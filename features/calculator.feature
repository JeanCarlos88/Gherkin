# language: pt
# Define o idioma da feature para português, permitindo usar palavras-chave em PT-BR

Funcionalidade: Calculadora Simples
  # História do Usuário (User Story) - Define o contexto e objetivo da funcionalidade
  # Formato: Como um [papel], Eu quero [ação], Para que [benefício]
  Como um usuário
  Eu quero realizar operações matemáticas básicas
  Para que eu possa fazer cálculos rapidamente

  # Cenário - Descreve um caso de teste específico
  # Deve ser claro, conciso e focado em um único comportamento
  Cenário: Soma de dois números positivos
    Dado que eu tenho o número 5
    E eu tenho o número 3
    Quando eu somar os números
    Então o resultado deve ser 8

  Cenário: Subtração de dois números
    Dado que eu tenho o número 10
    E eu tenho o número 4
    Quando eu subtrair os números
    Então o resultado deve ser 6

  # Esquema do Cenário - Permite testar múltiplas combinações de dados
  # Usa placeholders <variavel> que são substituídos pelos valores da tabela de Exemplos
  Esquema do Cenário: Multiplicação de números
    Dado que eu tenho o número <numero1>
    E eu tenho o número <numero2>
    Quando eu multiplicar os números
    Então o resultado deve ser <resultado>

    # Exemplos - Tabela de dados que será usada no Esquema do Cenário
    # Cada linha representa uma execução do cenário com diferentes valores
    Exemplos:
      | numero1 | numero2 | resultado |
      | 2      | 3      | 6         |
      | 4      | 5      | 20        |
      | 6      | 6      | 36        |