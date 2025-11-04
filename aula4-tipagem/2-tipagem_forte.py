"""
Tipagem Forte em Python

Em Python, a tipagem é forte. Isso significa que o interpretador não realiza 
conversões implícitas entre tipos de dados diferentes. Por exemplo, tentar 
concatenar uma string com um número inteiro resultará em um erro.
"""

print('b' + str(10))  # Correto: converte o inteiro 10 para string antes da concatenação
# print('b' + 10)  # Incorreto: gera um TypeError

print('Victor' + ' ' + 'Martins')  # Correto: concatena strings

print('Victor'.replace('t', ''))  # Correto: usa o método replace da string
# print('Victor' - 't')  # Incorreto: gera um TypeError