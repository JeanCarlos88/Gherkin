from behave import given, when, then
import re
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class User:
    name: str
    email: str
    password: str
    login_attempts: int = 0
    blocked: bool = False
    blocked_at: Optional[datetime] = None

class AuthenticationSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.current_user: Optional[User] = None
        self.max_login_attempts = 3
        self.sent_emails: List[Dict] = []

    def validate_password(self, password: str) -> tuple[bool, str]:
        if len(password) < 8:
            return False, "A senha deve ter no mínimo 8 caracteres"
        if not (re.search(r'[A-Za-z]', password) and re.search(r'[0-9]', password)):
            return False, "A senha deve conter letras e números"
        return True, ""

    def register_user(self, name: str, email: str, password: str) -> tuple[bool, str]:
        if email in self.users:
            return False, "Email já cadastrado"
        
        is_valid, message = self.validate_password(password)
        if not is_valid:
            return False, message

        self.users[email] = User(name=name, email=email, password=password)
        return True, "Cadastro realizado com sucesso"

    def login(self, email: str, password: str) -> tuple[bool, str]:
        if email not in self.users:
            return False, "Usuário não encontrado"

        user = self.users[email]
        if user.blocked:
            return False, "Conta bloqueada por segurança"

        if user.password != password:
            user.login_attempts += 1
            if user.login_attempts >= self.max_login_attempts:
                user.blocked = True
                user.blocked_at = datetime.now()
                self._send_recovery_email(user)
                return False, "Conta bloqueada por segurança"
            return False, "Senha incorreta"

        user.login_attempts = 0
        self.current_user = user
        return True, f"Bem-vindo, {user.name}"

    def logout(self):
        self.current_user = None

    def _send_recovery_email(self, user: User):
        self.sent_emails.append({
            "to": user.email,
            "subject": "Recuperação de conta",
            "type": "recovery"
        })

# Steps de contexto
@given('que o sistema está configurado')
def step_impl(context):
    context.auth_system = AuthenticationSystem()

@given('existe um banco de dados limpo')
def step_impl(context):
    context.auth_system.users.clear()

# Steps de cadastro
@given('que eu acesso a página de cadastro')
def step_impl(context):
    context.current_page = 'cadastro'

@when('eu preencho os seguintes dados')
def step_impl(context):
    context.form_data = {}
    for row in context.table:
        context.form_data[row['campo']] = row['valor']

@when('clico no botão "{button}"')
def step_impl(context, button):
    if button == "Cadastrar" and context.current_page == 'cadastro':
        success, message = context.auth_system.register_user(
            context.form_data['nome'],
            context.form_data['email'],
            context.form_data['senha']
        )
        context.result = {'success': success, 'message': message}

# Steps de login
@given('que existe um usuário cadastrado')
def step_impl(context):
    for row in context.table:
        context.auth_system.register_user(row['nome'], row['email'], row['senha'])

@given('o limite de tentativas é {limit:d}')
def step_impl(context, limit):
    context.auth_system.max_login_attempts = limit

@when('eu acesso a página de login')
def step_impl(context):
    context.current_page = 'login'

@when('preencho o campo "{field}" com "{value}"')
def step_impl(context, field, value):
    if not hasattr(context, 'form_data'):
        context.form_data = {}
    context.form_data[field] = value

@when('eu tento fazer login {attempts:d} vezes com a senha incorreta')
def step_impl(context, attempts):
    email = context.form_data.get('email', 'joao@exemplo.com')
    for _ in range(attempts):
        success, message = context.auth_system.login(email, 'senha_incorreta')
        context.result = {'success': success, 'message': message}

# Steps de verificação
@then('devo ver a mensagem "{message}"')
def step_impl(context, message):
    assert context.result['message'] == message, \
        f"Esperada mensagem '{message}', mas recebeu '{context.result['message']}'"

@then('devo ver a mensagem de erro "{message}"')
def step_impl(context, message):
    assert not context.result['success']
    assert context.result['message'] == message

@then('devo ser redirecionado para a página de {page}')
def step_impl(context, page):
    context.current_page = page

@then('a conta deve ser bloqueada')
def step_impl(context):
    user = context.auth_system.users[context.form_data['email']]
    assert user.blocked, "A conta deveria estar bloqueada"

@then('um email de recuperação deve ser enviado para "{email}"')
def step_impl(context, email):
    sent_emails = [e for e in context.auth_system.sent_emails 
                   if e['to'] == email and e['type'] == 'recovery']
    assert len(sent_emails) > 0, f"Nenhum email de recuperação foi enviado para {email}"

# Steps de logout
@given('que estou logado como "{name}"')
def step_impl(context, name):
    email = "joao@exemplo.com"  # Simplificado para o exemplo
    context.auth_system.register_user(name, email, "Senha123@")
    context.auth_system.login(email, "Senha123@")
    assert context.auth_system.current_user is not None

@then('não devo ter acesso às áreas protegidas')
def step_impl(context):
    assert context.auth_system.current_user is None