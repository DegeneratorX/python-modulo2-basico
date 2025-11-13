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
print("Fatiamento de 2 até 6:", nova_string)
nova_string = texto[:6] # começa do início e termina no 6. Irá imprimir "Python"
print("Fatiamento do início até 6:", nova_string)
nova_string = texto[4:] # começa do 4 e vai até o final. Irá imprimir "on s2"
print("Fatiamento do 4 até o final:", nova_string)
#######################################################

# Exemplo com índices negativos
nova_string = texto[-9:-3]  # Imprimirá python.
print("Fatiamento com índices negativos:", nova_string)

#########################################################

"""
Passo no fatiamento
- Podemos definir um passo no fatiamento.
- O passo indica de quantos em quantos índices a fatia irá pular.
- O valor padrão do passo é 1.
- Exemplo: texto[início:fim:passo]
"""

print(f"Imprime a string inteira: {texto[0:len(texto):1]}")  # Imprime a string inteira com passo 1. Normal
print(f"Imprime a string com passo 2: {texto[0:len(texto):2]}")  # Imprime a string inteira com passo 2. Pula de 2 em 2 caracteres
print(f"Imprime a string invertida: {texto[::-1]}")  # Imprime a string inteira com passo -1. Inverte a string
print(f"Imprime a string invertida com passo 2: {texto[::-2]}")  # Imprime a string inteira com passo -2. Inverte a string pulando de 2 em 2 caracteres

"""
As vezes não precisa colocar o início e o fim, apenas o passo.
"""

nova_string = texto[0::2]  # Pula de 2 em 2 letras.
print("Pula de 2 em 2 letras, não precisa especificar o fim:", nova_string)


"""
Cópia de string
- Para copiar uma string, podemos fatiar toda a string.
- Apenas atribuindo uma string a outra, ambas apontarão para o mesmo local na memória.
- A nova string será uma cópia da string original, e não apontará para o mesmo local na memória.
"""

copia_string = texto[:]  # Cópia da string inteira
print("Cópia da variável 'texto':", copia_string)

"""
Imutabilidade das strings
- Strings são imutáveis. Isso significa que não podemos alterar uma string existente.
- Qualquer operação que modifique uma string, na verdade cria uma nova string.
- Exemplos de operações que criam novas strings: fatiamento, concatenação, métodos
"""

try: # Tentando modificar a string diretamente
    texto[2] = 'X' # Strings são como tuplas, ou seja, imutáveis. Isso causará um erro.
except TypeError as e:
    print(f"Erro: {e}")

# A maneira correta de modificar uma string é criando uma nova string
nova_string = texto[:2] + 'X' + texto[3:]  # Criando uma nova string com a modificação desejada
print("Nova string após modificação:", nova_string)

# Outra forma de criar uma nova string é usando métodos de string
nova_string = texto.replace('s2', 'é legal!')  # Substituindo 's2' por 'é legal!'
print("Nova string após usar o método replace:", nova_string)

# Outra forma de criar é usando listas e o método join
# O problema é que o custo de memória é maior, pois cria uma lista temporária.
lista_caracteres = list(texto)  # Convertendo a string em uma lista de caracteres
lista_caracteres[2] = 'X'  # Modificando o caractere na lista
nova_string = ''.join(lista_caracteres)  # Juntando a lista de volta em uma string
print("Nova string após modificar via lista:", nova_string)