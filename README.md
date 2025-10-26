# Gherkin Testing Examples

Este projeto demonstra o uso do Gherkin para testes BDD (Behavior Driven Development) usando Python e Behave.

## Estrutura do Projeto

```
features/
├── steps/          # Implementações dos passos de teste
├── environment.py  # Hooks e configuração do ambiente
└── *.feature      # Arquivos de feature com cenários Gherkin
```

## Exemplos Incluídos

1. Básico: Calculadora simples
2. Intermediário: Carrinho de compras
3. Avançado: Autenticação de usuário com banco de dados

## Melhores Práticas do Gherkin

### 1. Estrutura Básica
```gherkin
Feature: [Nome da funcionalidade]
  As a [papel do usuário]
  I want to [objetivo]
  So that [benefício]

  Scenario: [Nome do cenário]
    Given [contexto inicial]
    When [ação]
    Then [resultado esperado]
```

### 2. Dicas de Escrita
- Use linguagem clara e objetiva
- Um cenário por comportamento
- Evite detalhes técnicos nas features
- Use dados relevantes para o negócio
- Mantenha os cenários curtos e focados

### 3. Padrões Recomendados
- Given: Define o contexto inicial
- When: Descreve a ação principal
- Then: Especifica o resultado esperado
- And/But: Para passos adicionais do mesmo tipo

### 4. Antipadrões a Evitar
- Não misture detalhes técnicos nas features
- Evite cenários muito longos
- Não repita steps desnecessariamente
- Evite dependência entre cenários

## Como Executar os Testes

1. Instale as dependências:
```bash
pip install behave pytest selenium
```

2. Execute os testes:
```bash
behave
```

Para executar uma feature específica:
```bash
behave features/calculator.feature
```