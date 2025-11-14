"""
Listas em Python

São dados mutáveis, ou seja, podem ser alterados após sua criação.

No python é possível colocar diferentes tipos de dados em uma mesma lista.
Isso só é possível porque a lista guarda referências para os objetos na memória,
e não exatamente os objetos em si. Ou seja, uma lista contém apenas endereços.

Existem várias operações em listas, como:
- fatiamento, append, insert, pop, del, clear, etend, +
- min, max
- range
"""

#         0    1    2    3    4
lista = ["A", "B", "C", "D", "E"]
#        -5   -4   -3   -2   -1

string = "ABCDE"

print("Acessando índice 1 da string:", string[1])  # Acessa o índice (caractere) da string.
print("Acessando índice 1 da lista:", lista[1])  # Acessa o índice (caractere) da lista.

# A diferença é que na lista, você consegue pegar até palavras. Exemplo:

lista_palavras = ["Lab", "Python", "Olá"]
print("Acessando índice 1 da lista de palavras:", lista_palavras[1])  # Printará "Python".

# E você consegue também mudar valores na lista, diferente da string, que é imutável.

lista_palavras[0] = "Laboratório"
print("Lista de palavras após alteração do índice 0:", lista_palavras)  # Printará ['Laboratório', 'Python', 'Olá'].


print("\n###################################\n")

texto = "Valor"
num = 2
listaExemplo = [1, num, 3, 4, "Victor", True, 10.5]  # É como se fosse uma variável com vários valores dentro dela
print("Lista exemplo:", listaExemplo)  # Printa a lista toda.


print("Veja como a referência é a mesma:", id(num), id(listaExemplo[1])) # Mostra que o endereço do num e o endereço do índice 1 da lista são os mesmos.

"""
Listas Multidimensionais - listas dentro de listas

As listas podem conter outras listas, formando listas multidimensionais, ou Matrizes.
"""

matriz = [[1,2,3], [4,5,6], [7,8,9]]  # lista 2D (matriz 3x3)
print("Lista matriz (2D):", matriz)
print("Acessando o elemento na linha 1, coluna 2:", matriz[1][2])  # acessa o elemento 6

# printando a matriz de forma estruturada
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # nova linha após cada linha da matriz