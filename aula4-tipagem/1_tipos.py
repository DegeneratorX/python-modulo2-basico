"""
Tipos de dados
str - string (textos)
int - inteiro (123456 0 -10 -1500 0)
foat - real/ponto flutuante (0.0 10.5 -15.4)
bool - booleano/lógico (0 e 1, False/True)
"""

print('Victor', type('Victor'))
print(10, type(10))
print(12.4, type(12.4))

print(True, type(True))
print(10 == 10, type(10 == 10))
print('Victor' == 'Vitor', type('Victor' == 'Vitor'))
print(bool(""),type(bool("")))  # string vazia avalia em False
print(bool(0),type(bool(0)))  # 0 é considerado False pelo bool
print(bool([]),type(bool([])))  # array vazio é considerado Falso

print('10', type('10'), type(int('10')))  # Conversão de str pra int apenas pra leitura

# print('victor', int('victor')) dá erro.
# print('10.3', int('10.3')) dá erro.

# Nome: str
print('Victor Martins', type('Victor Martins'))

# Idade: int
print(25, type(25))

# Altura: float
print(1.83, type(1.83))

# É maior de idade x>18
print(32>18, type(32>18))