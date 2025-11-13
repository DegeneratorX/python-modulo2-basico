"""
Operador or em Python

O operador or retorna o primeiro valor verdadeiro (truthy) que encontrar
ou o último valor, caso todos sejam falsos (falsy).
"""

# Forma tradicional

nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada.')  # String vazia = false.

############################

# Forma reduzida

print("Forma reduzida:", nome or 'Você não digitou nada.')

################################

print("\n################################\n")


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Victor'

if a:
    variavel = a
elif b:
    variavel = b
elif c:
    variavel = c
elif d:
    variavel = d
elif e:
    variavel = e
elif f:
    variavel = f
else:
    variavel = g

print("Primeiro valor true encontrado:", variavel)

# Forma reduzida com or

variavel = a or b or c or d or e or f or g # retorna 22, pois é o primeiro valor verdadeiro (truthy)
print("Primeiro valor true encontrado (forma reduzida):", variavel)
