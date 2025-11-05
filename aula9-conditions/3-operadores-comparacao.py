"""
Operadores de comparação

== igualdade
>= maior ou igual
> maior que
< menor que
<= menor ou igual
!= diferente


"""

print(2 == 2)  # Retornará True

print(2 == 1)  # Retornará False

print(2 == '2')  # Retornará False, pois String != Int

########################################

num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 == num_2)  # O operador == é uma função (bem baixo nível e 
# visualmente implícita) que pergunta se é verdadeiro ou falso e atribui a variável
# "expressao"

print(expressao)  # True

expressao = (num_1 > num_2) # O mesmo vale para os outros operadores matemáticos

print(expressao)  # False

##########################################

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 80

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')


##########################################
# Operadores de comparação podem ser encadeados
print(10 > 5 > 3 > 1)  # True
print(10 > 5 > 30 > 1)  # False
print(10 == 10 <= 10 >= 9 < 11 != 5)  # True
print(10 == 10 <= 10 >= 9 < 11 != 10)  # False

##########################################
# Comparando strings
print('Victor' == 'Victor')  # True
print('Victor' == 'Vitor')  # False
print('Victor' > 'Vitor')  # True, pois 'c' vem depois de 't' na tabela ASCII.
print('Victor' < 'Vitor')  # False
print('a' > 'A')  # True, letras maiúsculas vêm antes das minúsculas na tabela ASCII
print('a' < 'A')  # False

##########################################
# Comparando diferentes tipos
print(10 == 10.0)  # True, int e float podem ser comparados
print(10 == '10')  # False, int e str não são comparáveis
print(1 == True)  # True, bool é um subtipo de int (True é 1, False é 0)
print(0 == False)  # True   
print(2 == True)  # False, pois 2 não é igual a 1
print(3 != True)  # True, pois 3 não é igual a 1

##########################################
# Cuidado com comparações inválidas
# print('10' > 5)  # Erro: TypeError
# print('Victor' < 10)  # Erro: TypeError
# print(True > 'False')  # Erro: TypeError
# print(None == 0)  # False, mas não é recomendado comparar com None dessa forma
# print(None > 0)  # Erro: TypeError
# print(None < 0)  # Erro: TypeError

# Use 'is' para comparar com None
print(None is None)  # True
print(None is not None)  # False