"""
Split, Join, Enumerate
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # iteráveis
"""

string = 'O Brasil é penta.'
lista = string.split(' ')  # Separa a string em uma lista

print(lista)

string2 = ','.join(lista)  # transforma a lista em uma string, unindo com vírgulas.

print(string2)
