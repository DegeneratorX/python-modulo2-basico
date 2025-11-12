"""
Manipulando Strings

-String íncides
-Fatiamento de strings [inicio:fim:passo]
-Funções built-in len, abs, type, print etc...
"""

# As strings são listas imutáveis de caracteres. Listas serão vistas mais a frente.
# Cada caractere da string possui um índice. O índice inicia em 0 (zero).
# Para acessar os caracteres da string, usamos o índice entre colchetes [].

# positivos    [012345678]   <--- Índices de cada letra da string abaixo.
texto        = 'Python s2'
# negativos   -[987654321]

print(texto[2])  # índice 2. Aparecerá a letra 't', pois o índice é 2, como mostrado acima.

######################################################

"""
Fatiamento de strings [início:fim:passo]
- O fatiamento de strings funciona como em listas (que serão vistas mais a frente).
- O valor do índice "fim" não é incluído no resultado final.
- Sempre que fatia, é feita uma cópia da string original.
"""
# Fatiamento de strings
nova_string = texto[2:6]  # começa do 2 e termina no 6. Irá imprimir "thon"
print(nova_string)
nova_string = texto[:6] # começa do início e termina no 6. Irá imprimir "Python"
print(nova_string)

#######################################################

# Exemplo com índices negativos
nova_string = texto[-9:-3]  # Imprimirá python.
print(nova_string)

#########################################################

"""
Cópia de string
- Para copiar uma string, podemos fatiar toda a string.
- Apenas atribuindo uma string a outra, ambas apontarão para o mesmo local na memória.
- A nova string será uma cópia da string original, e não apontará para o mesmo local na memória.
"""

copia_string = texto[:]  # Cópia da string inteira