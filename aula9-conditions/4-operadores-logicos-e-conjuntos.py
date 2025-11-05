"""
Operadores Lógicos

and, or, not
in, not in
"""

a = 2
b = 3

if not b>a:  # not = ! = inverte o operador.
    print('A é maior do que B')
else:
    print('B é maior do que A')

a = ''  # Vazio. Valor booleano FALSE.
b = 0  # Zero inteiro tem valor booleano FALSE.

if not a:  # Checa pra ver se está vazio. Como está, será FALSE, mas como tem "not", o if é lido, pois agora é TRUE
    print('Por favor, preencha o valor de A.')

if not b:  # Checa pra ver se está vazio. Como está, será FALSE, mas como tem "not", o if é lido, pois agora é TRUE
    print('Por favor, preencha o valor de A.')

#####################################

nome = 'Victor'

if 'u' in nome:
    print('Existe a letra U no seu nome')
else:
    print('Não existe a letra U no seu nome.')

######################################

if 'tor' in nome:
    print('Existe "tor" no seu nome.')
else:
    print('Não existe "tor" no seu nome')

########################################

if 'asas' not in nome:
    print('Esse comando será executado')
else:
    print("Se isso aqui executar, é um milagre. Mas existe 'asas' na palavra.")



