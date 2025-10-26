from behave import given, when, then
from decimal import Decimal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = Decimal(str(price))

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = Decimal('0')
        self.discount = None

    def add_item(self, product, quantity=1):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {
                'product': product,
                'quantity': quantity
            }
        self._calculate_total()

    def remove_item(self, product_name):
        if product_name in self.items:
            del self.items[product_name]
            self._calculate_total()

    def apply_discount(self, percentage):
        self.discount = percentage
        self._calculate_total()

    def _calculate_total(self):
        self.total = Decimal('0')
        for item in self.items.values():
            self.total += item['product'].price * item['quantity']
        
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
        
        self.total = self.total.quantize(Decimal('0.01'))

@given('que eu tenho um carrinho de compras vazio')
def step_impl(context):
    context.cart = ShoppingCart()
    context.products = {}

@given('os seguintes produtos disponíveis')
def step_impl(context):
    for row in context.table:
        name = row['nome']
        price = Decimal(row['preco'])
        context.products[name] = Product(name, price)

@given('que eu tenho os seguintes itens no carrinho')
def step_impl(context):
    for row in context.table:
        product_name = row['produto']
        quantity = int(row['quantidade'])
        product = context.products[product_name]
        context.cart.add_item(product, quantity)

@given('existe um cupom "{cupom}" de {percentage:d}% de desconto')
def step_impl(context, cupom, percentage):
    context.coupons = {cupom: percentage}

@when('eu adiciono "{product_name}" ao carrinho')
def step_impl(context, product_name):
    product = context.products[product_name]
    context.cart.add_item(product)

@when('eu removo "{product_name}" do carrinho')
def step_impl(context, product_name):
    context.cart.remove_item(product_name)

@when('eu aplico o cupom "{cupom}"')
def step_impl(context, cupom):
    if cupom in context.coupons:
        context.cart.apply_discount(context.coupons[cupom])

@then('o carrinho deve conter {count:d} item(ns)')
def step_impl(context, count):
    assert len(context.cart.items) == count, \
        f"Esperado {count} itens, mas encontrou {len(context.cart.items)}"

@then('o valor total deve ser R$ {total:g}')
def step_impl(context, total):
    expected_total = Decimal(str(total)).quantize(Decimal('0.01'))
    assert context.cart.total == expected_total, \
        f"Esperado R$ {expected_total}, mas obteve R$ {context.cart.total}"