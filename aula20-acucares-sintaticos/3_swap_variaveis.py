"""
Inverter valores entre variáveis em Python.
"""

# Forma mais tradicional possível de inverter valores entre variáveis.

x = 10
y = 'Victor'

z = x # variável temporária z para guardar o valor de x
x = y
y = z

print(f'x = {x} e y = {y}')

############################
print("\n############################\n")

# Método super simples e prático para inverter!

a = 10
b = 'Victor'

a, b = b, a # desempacotamento de tupla para inverter os valores (não precisa de variável temporária)

print(f'a = {a} e b = {b}')