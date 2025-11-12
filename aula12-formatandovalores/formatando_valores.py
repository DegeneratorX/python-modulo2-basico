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

# Caso extremo
"""
O resultado do número 1150.54156487 com 0=+10,.1f é +001,150.5
O que acontece aqui é o seguinte:

1. O número 1150.54156487 é formatado para ter 1 casa decimal, resultando em 1150.5.
2. O sinal de positivo (+) é adicionado antes do número, resultando em +1150.5.
3. O total de caracteres desejados é 10. Atualmente, o número +1150.5 tem 7 caracteres (incluindo o sinal e o ponto decimal).
4. Para completar os 10 caracteres, são adicionados 3 zeros (0) à esquerda do número, resultando em +001,150.5.
5. Além disso, um separador de milhar (vírgula) é adicionado para melhorar a legibilidade, resultando em +001,150.5.
"""
num_3 = 1150.54156487
print(f'{num_3:0=+10,.1f}')