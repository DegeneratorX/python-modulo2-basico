"""
Manipulando Strings

-String íncides
-Fatiamento de strings [inicio:fim:passo]
-Funções built-in len, abs, type, print etc...
"""

# positivos    [012345678]   <--- Índices de cada letra da string abaixo.
texto        = 'Python s2'
# negativos   -[987654321]

nova_string = texto[0::2]  # Pula de 2 em 2 letras.
print(nova_string)

nova_string = texto[0::3]  # Pula de 3 em 3 letras.
print(nova_string)
