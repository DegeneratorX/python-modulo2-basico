"""
+,-,*,/

// divisão inteira (arredonda)
** exponenciação (potenciação)
% resto da divisão (módulo)
() parênteses de prioridades
"""

print('Multiplicação', 10 * 10) # retorna 100
print('Adição', 10 + 10) # retorna 20
print('Subtração', 10 - 5) # retorna 5
print('Divisão', 10 / 2) # retorna 5.0 (sempre float)

print('Multiplicação especial', 5 * '10')  # repete a string "10" cinco vezes.
print('Adição especial', '5' + '10')  # Junta a string 5 com 10, formando a string 510.

# O '//' realiza uma divisão inteira, ou seja, arredonda o resultado para baixo.
print('Divisão inteira', 10//3) # retorna 3
print('Divisão inteira', 11.2//3)  # Nesse caso retorna um float, pois existe um float na expresão. Resulta em 3.0

print('\nExponenciação', 3**3) # 3 elevado a 3 (3x3x3)

print('Ordem de precedência', 10 + 5 * 2)  # retorna 20 (multiplicação antes da adição

print('Ordem de precedência com parênteses', (10 + 5) * 2)  # retorna 30 (parênteses alteram a ordem)

#########################################

# Aqui estão alguns exemplos de uso do operador módulo (%)
print("\nResto da divisão (módulo)")
print('Resto da divisão', 10 % 3)  # retorna 1 (10 dividido por 3 dá 3, sobra 1)
print('Resto da divisão', 11 % 2)  # retorna 1 (11 dividido por 2 dá 5, sobra 1)
print('Resto da divisão', 12 % 2)  # retorna 0 (12 dividido por 2 dá 6, sobra 0)
print('Resto da divisão', 15 % 4)  # retorna 3 (15 dividido por 4 dá 3, sobra 3)

# E aqui a sua utilização para saber se um número é múltiplo de outro.
print('\nVerificando múltiplos usando o módulo')
print('15 É múltiplo de 2 (par)?', 15 % 2 == 0)  # retorna False (15 não é múltiplo de 2). Além disso, verifica se o número é par.
print('10 É múltiplo de 2 (par)?', 10 % 2 == 0)  # retorna True (10 é múltiplo de 2). Além disso, verifica se o número é par.
print('15 É múltiplo de 3?', 15 % 3 == 0)  # retorna True (15 é múltiplo de 3)
print('15 É múltiplo de 4?', 15 % 4 == 0)  # retorna False (15 não é múltiplo de 4)
print('15 É múltiplo de 5?', 15 % 5 == 0)  # retorna True (15 é múltiplo de 5)
print('15 É múltiplo de 6?', 15 % 6 == 0)  # retorna False (15 não é múltiplo de 6)