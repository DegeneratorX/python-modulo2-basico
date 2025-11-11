"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Ponto Flutuante (float)
:.(NÚMERO)F - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

# Sem formatação
print(f"Resultado da divisão: {divisao}")

# Com formatação de 2 casas decimais (já foi visto)
print(f"Resultado da divisão: {divisao:.2f}")

###########################

# Formatações com modificadores
num_1 = 1
print(f'{num_1:0>10}') # Adiciona 0s à esquerda, totalizando 10 caracteres


num_2 = 1150
print(f'{num_2:0>10}') # Adiciona 0s à esquerda, totalizando 10 caracteres

print(f'{num_2:0^10}') # Adiciona 0s ao centro, totalizando 10 caracteres

titulo = "BeM viNdO"

print(f'{titulo:=^20}') # Adiciona = ao centro, totalizando 20 caracteres

print(f'{num_2:0^10.2f}') # Adiciona 0s ao centro, totalizando 10 caracteres, com 2 casas decimais

print(titulo.lower())  # Deixa tudo minúsculo
print(titulo.upper())  # Deixa tudo maiúsculo
print(titulo.title())  # Primeiras letras maiúsculas
