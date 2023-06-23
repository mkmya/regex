import re

def valid_email(email):
    regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    if bool(re.match(regex, email)):
        print(f'Parabéns! O e-mail "{email}" foi cadastrado com sucesso!')
    else:
        print(f'Erro! O e-mail "{email}" é inválido.')

valid_email('marina@gmail.com')
valid_email('marina')