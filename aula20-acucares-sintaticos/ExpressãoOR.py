# Forma tradicional

nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada.')  # String vazia = false.

############################

# Forma reduzida

print(nome or 'Você não digitou nada!')

################################

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Victor'

variavel = a or b or c or d or e or f or g
print(variavel)

"""Isso tudo poupa a seguinte linha de código:"""
"""
if a:
    variavel = a
elif b:
    variavel = b
elif c................
.
.
"""
