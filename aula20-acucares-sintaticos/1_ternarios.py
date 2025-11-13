"""
Operador Ternário em Python

<valor> if <condição> else <outro_valor>
"""

# Tradicional forma

logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print("Mensagem:", msg)

#################################

# Alternativa: usando operador ternário

msg2 = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg2)

###################################

# Outro exemplo de forma tradicional

idade = int(input('Qual a sua idade? '))

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar')

###################################

# Forma alternada com operador ternário

idade2 = int(input('Qual a sua idade? '))

e_de_maior = (idade2 >= 18)  # True ou False
msg3 = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

print(msg3)
