from behave import given, when, then

class Calculator:
    def __init__(self):
        self.numbers = []
        self.result = None

    def add(self):
        self.result = sum(self.numbers)
        return self.result

    def subtract(self):
        if len(self.numbers) >= 2:
            self.result = self.numbers[0] - self.numbers[1]
        return self.result

    def multiply(self):
        if len(self.numbers) >= 2:
            self.result = self.numbers[0] * self.numbers[1]
        return self.result

@given('que eu tenho o número {number:d}')
def step_impl(context, number):
    if not hasattr(context, 'calculator'):
        context.calculator = Calculator()
    context.calculator.numbers.append(number)

@when('eu somar os números')
def step_impl(context):
    context.calculator.add()

@when('eu subtrair os números')
def step_impl(context):
    context.calculator.subtract()

@when('eu multiplicar os números')
def step_impl(context):
    context.calculator.multiply()

@then('o resultado deve ser {result:d}')
def step_impl(context, result):
    assert context.calculator.result == result, f"Esperado {result}, mas obteve {context.calculator.result}"