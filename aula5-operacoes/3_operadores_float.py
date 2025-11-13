"""
Imprecisão com números de ponto flutuante (float).
"""

import decimal

n1 = 0.1
n2 = 0.7
res = n1 + n2

print('Resultado impreciso 0.1 + 0.7:', res)  # Espera-se 0.8, mas retorna 0.7999999999999999
print('Comparação imprecisa:', res == 0.8)  # Retorna False devido à imprecisão

print("\n################################\n")
"""
Arredondamentos

É possível arredondar o valor utilizando a função built-in round(), ou utilizar
a biblioteca math para piso e teto.
"""

print('Valor arredondado:', round(res, 2))  # Arredonda o resultado para 2 casas decimais
print('Comparação arredondada:', round(res, 2) == 0.8)  # Agora retorna True

import math
print('Valor arredondado com math:', math.ceil(res))  # Arredonda para cima
print('Valor arredondado com math:', math.floor(res))  # Arredonda para baixo
print('Valor arredondado com math:', math.trunc(res))  # Trunca (corta) a parte decimal


print("\n################################\n")

"""
Biblioteca decimal

Para maior precisão em operações de float, utiliza-se a biblioteca decimal.
A ideia é evitar a imprecisão dos floats nas operações, algo comum em muitas 
linguagens de programação.
"""

n1_decimal = decimal.Decimal('0.1') # Cria um decimal a partir de string para evitar imprecisão
n2_decimal = decimal.Decimal('0.7')
res_decimal = n1_decimal + n2_decimal
print('Resultado com decimal 0.1 + 0.7:', res_decimal)  # Retorna exatamente 0.8
print('Comparação com decimal:', res_decimal == decimal.Decimal('0.8'))  # Retorna True