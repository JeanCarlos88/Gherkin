# language: pt
# Define o idioma da feature para português

Funcionalidade: Carrinho de Compras
  # História do Usuário - Define o propósito da funcionalidade
  # Descreve quem (papel), o que (ação) e por que (benefício)
  Como um cliente
  Eu quero gerenciar meu carrinho de compras
  Para que eu possa controlar minhas compras antes de finalizar

  # Contexto - Define o estado inicial comum a todos os cenários
  # Evita repetição de passos e torna os cenários mais limpos
  Contexto:
    Dado que eu tenho um carrinho de compras vazio
    # Tabela de Dados - Fornece dados estruturados para os testes
    # Facilita a manutenção e visualização dos dados de teste
    E os seguintes produtos disponíveis:
      | nome      | preco  |
      | Camiseta  | 49.90  |
      | Calça     | 89.90  |
      | Tênis     | 199.90 |

  Cenário: Adicionar produto ao carrinho
    Quando eu adiciono "Camiseta" ao carrinho
    Então o carrinho deve conter 1 item
    E o valor total deve ser R$ 49.90

  Cenário: Adicionar múltiplos produtos ao carrinho
    Quando eu adiciono "Camiseta" ao carrinho
    E eu adiciono "Calça" ao carrinho
    Então o carrinho deve conter 2 itens
    E o valor total deve ser R$ 139.80

  Cenário: Remover produto do carrinho
    Dado que eu tenho os seguintes itens no carrinho:
      | produto   | quantidade |
      | Camiseta  | 2         |
      | Calça     | 1         |
    Quando eu removo "Camiseta" do carrinho
    Então o carrinho deve conter 1 item
    E o valor total deve ser R$ 89.90

  # Cenário com múltiplos passos e dados complexos
  # Demonstra como testar regras de negócio mais elaboradas
  Cenário: Aplicar cupom de desconto
    # Dado (Given) - Define o estado inicial específico deste cenário
    Dado que eu tenho os seguintes itens no carrinho:
      | produto   | quantidade |
      | Tênis     | 1         |
    # E (And) - Adiciona condições adicionais ao contexto
    E existe um cupom "DESCONTO10" de 10% de desconto
    # Quando (When) - Define a ação principal sendo testada
    Quando eu aplico o cupom "DESCONTO10"
    # Então (Then) - Verifica o resultado esperado
    Então o valor total deve ser R$ 179.91