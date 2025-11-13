"""
Operador Ternário em Python
"""

# Tradicional forma

logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

#################################

# Usando operador ternário

msg2 = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg2)

###################################

# Forma tradicional

idade = int(input('Qual a sua idade? '))

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar')

###################################

idade2 = int(input('Qual a sua idade? '))

e_de_maior = (idade2 >= 18)  # True ou False
msg3 = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

print(msg3)
