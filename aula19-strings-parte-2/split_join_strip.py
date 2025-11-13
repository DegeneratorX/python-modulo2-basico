"""
Split, Join, Strip
"""

"""
Split - Dividir uma string
"""

string = "O Brasil é o país do futebol, o Brasil é penta."

# A função split divide uma string e gera uma lista.

lista_1 = string.split(' ')  # O espaço representa o que será "pego" pra dividir a lista.

print("Lista formada a partir da lista_1:", lista_1)  # Resultado: o python detectou os espaços, e eliminou eles e separou em palavras a partir dos espaços.

lista_2 = string.split(',')  # Agora o python detectará alguma vírgula, eliminará essa vírgula e criará duas partições.

print("Lista formada a partir da lista_2:", lista_2)  # Resultado: duas strings, uma antes da vírgula e outra depois.
###########################################################
print("\n##########################################\n")

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')  # .count(valor) conta as vezes que a palavra
    #                                                                         'valor' apareceu dentro da lista_1.

##########################################
print()

palavra = ""
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

##########################################
print("\n##########################################\n")

"""
.join - Junta uma lista em uma string
"""

string_2 = 'O Brasil é penta.'
lista = string_2.split(' ')  # Separa a string em uma lista

print("string_2 splitada:", lista)

string_nova = ','.join(lista)  # transforma a lista em uma string, unindo com vírgulas.

print(string_nova)


##########################################
print("\n##########################################\n")

"""
strip - Remove espaços no começo e fim da string
"""

# A função strip remove os espaços no começo e fim da string. Capitalize coloca maiúscula a primeira letra da frase.
for valor in lista_2:
    print(valor.strip().capitalize())

