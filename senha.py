import re

def check_password(password):
    if len(password) < 8:
        return "senha muito curta. Deve conter 8 caracteres"
    elif not re.search("[a-z]", password):
        return "senha deve conter pelo menos 1 letra minúscula"
    elif not re.search("[A-Z]", password):
        return "senha deve conter pelo menos 1 letra maiúscula"
    elif not re.search("[0-9]", password):
        return "senha deve conter pelo menos 1 número"
    elif not re.search("[!@#$%¨&*(),.?{}|<>]", password):
        return "senha deve conter pelo menos 1 caractere especial"
    else:
        return "senha ok"

# Dicionário de usuários (nome de usuário)

usuarios = {
    "santiago",
}

def check_user(username):

    #se o nome de usuario exister em usuarios ele pede a senha se nao ele retorna que o usuario não foi encontrada

    if username in usuarios:
        senha = input("Digite a senha: ")
        result = check_password(senha)
        return result
    else:
        return "Acesso negado: usuário não encontrado"



username = input("Digite o nome de usuário: ")


# Verificar o acesso
resultado = check_user(username)
print(resultado)
