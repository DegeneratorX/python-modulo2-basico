# Forma mais tradicional possível de inverter valores entre variáveis.

x = 10
y = 'Victor'

z = x
x = y
y = z

print(f'x = {x} e y = {y}')

############################

# Método super simples e prático para inverter!

a = 10
b = 'Victor'
c = 'Olá'

a, b, c = c, a, b

print(f'a = {a} e b = {b} e c = {c}')
