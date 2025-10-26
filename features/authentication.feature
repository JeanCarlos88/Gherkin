# language: pt
# Define o idioma da feature, permitindo usar palavras-chave em português

# @autenticacao - Tag que permite agrupar e filtrar cenários relacionados
@autenticacao
Funcionalidade: Sistema de Autenticação
  # User Story no formato "Como... Eu quero... Para que..."
  # Descreve o valor de negócio da funcionalidade
  Como um usuário do sistema
  Eu quero poder me autenticar
  Para que eu possa acessar áreas protegidas

  # Regras de Negócio - Definem os requisitos específicos que devem ser atendidos
  Regra: Senha deve ter no mínimo 8 caracteres
  Regra: Senha deve conter letras e números

  # Antecedentes (Background) - Configuração comum executada antes de cada cenário
  # Evita repetição de passos em múltiplos cenários
  Antecedentes:
    Dado que o sistema está configurado
    E existe um banco de dados limpo

  @cadastro
  Cenário: Cadastro de novo usuário com sucesso
    Dado que eu acesso a página de cadastro
    Quando eu preencho os seguintes dados:
      | campo                  | valor                |
      | nome                  | João Silva           |
      | email                 | joao@exemplo.com     |
      | senha                 | Senha123@            |
      | confirmacao_senha     | Senha123@            |
    E clico no botão "Cadastrar"
    Então devo ver a mensagem "Cadastro realizado com sucesso"
    E devo ser redirecionado para a página de login

  @cadastro @validacao
  Esquema do Cenário: Tentativa de cadastro com senha inválida
    Dado que eu acesso a página de cadastro
    Quando eu preencho os seguintes dados:
      | campo                  | valor                |
      | nome                  | João Silva           |
      | email                 | joao@exemplo.com     |
      | senha                 | <senha>              |
      | confirmacao_senha     | <senha>              |
    E clico no botão "Cadastrar"
    Então devo ver a mensagem de erro "<mensagem>"

    Exemplos:
      | senha     | mensagem                                        |
      | 123456    | A senha deve ter no mínimo 8 caracteres        |
      | abcdefgh  | A senha deve conter letras e números           |
      | 12345678  | A senha deve conter letras e números           |

  @login
  Cenário: Login com sucesso
    Dado que existe um usuário cadastrado:
      | nome      | email             | senha     |
      | João Silva| joao@exemplo.com  | Senha123@ |
    Quando eu acesso a página de login
    E preencho o campo "email" com "joao@exemplo.com"
    E preencho o campo "senha" com "Senha123@"
    E clico no botão "Entrar"
    Então devo ser redirecionado para a página inicial
    E devo ver a mensagem "Bem-vindo, João Silva"

  @login @seguranca
  Cenário: Bloqueio após tentativas incorretas
    Dado que existe um usuário cadastrado:
      | nome      | email             | senha     |
      | João Silva| joao@exemplo.com  | Senha123@ |
    E o limite de tentativas é 3
    Quando eu tento fazer login 3 vezes com a senha incorreta
    Então a conta deve ser bloqueada
    E devo ver a mensagem "Conta bloqueada por segurança"
    E um email de recuperação deve ser enviado para "joao@exemplo.com"

  @logout
  Cenário: Logout do sistema
    Dado que estou logado como "João Silva"
    Quando eu clico no botão "Sair"
    Então devo ser redirecionado para a página de login
    E não devo ter acesso às áreas protegidas