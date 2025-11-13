"""
Listas - Métodos e funções
"""

"""
Fatiamento de listas [início:fim:passo]
"""
#         0    1    2    3    4     5
lista = ["A", "B", "C", "D", "E", 10.5]
lista[5] = "Qualquer coisa"  # Substitui o índice 5, que contém o float 10.5, e guarda essa string.

print("Print da lista:", lista[5])
print("Índices 0 a 2:", lista[0:3:])  # Será exibido o que estiver no índice 0, 1 e 2. Não inclui o 3.
print("Pula de 2 em 2:", lista[::2])  # Pula de 2 em 2

print("###################################")

"""
Concatenação de listas com +
"""
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print("Lista 1:", l1)
print("Lista 2:", l2)
print("Lista 3 (concatenação de l1 e l2):", l3)  # Imprimirá [1,2,3,4,5,6]. É uma forma de juntar listas, mas não é a melhor.


print("###################################")

"""
.extend(x) - insere uma lista dentro de outra.
A diferença com a concatenação é que o extend modifica a lista original, enquanto o + cria uma nova lista.
"""

l1.extend(l2)  # mesmo resultado de l3
print("Lista 1 após extend com l2:", l1)
l1.extend('a')  # "adiciona" 'a' a lista. O problema é que a função extend não é adequada para adição, e sim pra juntar.
print("Lista 1 após extend com a letra 'a':", l1)

print("###################################")

"""
.append(x) - adiciona um elemento ao final da lista.
"""

l1.append('b')  # adiciona b ao final da lista de forma apropriada.
print("Lista 1 após append com a letra 'b':", l1)
print("l1[7]:", l1[7])  # agora tem 8 índices, sendo o índice 7 o valor b.

print("###################################")

"""
.insert(i, x) - insere um elemento x na posição i da lista.
OBS: O insert não substitui o valor do índice, ele empurra os outros valores para frente.
"""

l2.insert(1, 'banana')  # o insert adiciona em qualquer lugar da lista. Recebe o valor do índice pra adicionar. O resto
#                         é empurrado pra frente.
print("l2 após insert de 'banana':", l2)
print("l2[1]:", l2[1])


print("###################################")

"""
.pop(i) - remove o elemento do índice i da lista e o retorna.
Se não for passado o índice i, o pop remove o último elemento da lista.
"""

l2.pop()  # o pop retira o último elemento da lista.
print("l2 após pop:", l2)

print("###################################")

"""
del - remove um elemento de um índice específico.
Não há necessidade de usar parênteses para o del, pois não é uma função, e sim um comando.
"""

#     0 1 2 3 4 5 6 7 8
l4 = [1,2,3,4,5,6,7,8,9]

del(l4[3:5])  # excluirá entre 3 e 6.
print("l4 após del entre os índices 3 e 5:", l4)
del l4[0:5]   # excluirá entre 0 e 4.
print("l4 após del entre os índices 0 e 4:", l4)

print("###################################")

"""
max() e min() - retornam o maior e o menor valor da lista, respectivamente.
Para listas com strings, ele retorna o maior e o menor valor considerando a ordem alfabética.
Para listas com diferentes tipos de dados, pode gerar erro.
"""

l5 = [91,23,56,38,43,37]

print("Lista l5:", l5)
print("maior:", max(l5))  # Maior valor da lista (inteiro)
print("menor:", min(l5))  # Menor valor da lista (inteiro)

print("###################################")

try: 
    l6 = ['banana', 'abacaxi', 1, 'uva']
    print("Lista l6:", l6)
    print("maior:", max(l6))  # Maior valor da lista (string)
    print("menor:", min(l6))  # Menor valor da lista (string)
except TypeError as e:
    print("Erro ao comparar diferentes tipos de dados na lista:", e)

print("###################################")

"""
range() - cria uma lista de números inteiros em um intervalo determinado.
"""

l7 = range(1,10)  # Função range() do laço for. Percorre 1 até 9.
print(l7)  # Normalmente não acontece nada. Ele simplesmente printa a função.

l7 = list(range(1,10))  # Mas se eu adicionar a função list a função iterável range, eu converto pra lista.
print(l7)  # E com isso não precisa digitar 123...89 dentro de uma lista.

print("###################################")

"""
Estrutura de repetição for com listas
"""

l8 = ['String', True, 10, -20.5]
 
for elemento in l8:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')


print("###################################")

"""
sort() - ordena os elementos da lista in loco (modifica a lista original).
sorted() - retorna uma nova lista ordenada a partir de uma lista existente.
A diferença entre o sorted() e o .sort() é que o sorted() retorna uma nova lista, enquanto o .sort() modifica a lista original.
O algoritmo de sort é mais eficiente que o de sorted, pois o sorted precisa criar uma nova lista na memória.
O algoritmo utilizado para ordenação em ambos os casos é o Timsort, que é uma combinação de Merge Sort e Insertion Sort.
"""

l9 = [5,3,8,1,4]
print("Lista l9 original:", l9) 
l9.sort()  # ordena a lista l9
print("Lista l9 após .sort():", l9)

l10 = [7,2,9,6,0]
print("Lista l10 original:", l10) 
l11 = sorted(l10)  # cria uma nova lista ordenada a partir de l10
print("Lista l10 após sorted():", l10)
print("Nova lista l11 criada com sorted() a partir de l10:", l11) # Mais custoso em termos de memória, mas não modifica a lista original.

l12 = ['banana', 'abacaxi', 'uva', 'laranja']
print("Lista l12 original:", l12) 
l12.sort()  # ordena a lista l12
print("Lista l12 após .sort():", l12)

l13 = ['banana', 'abacaxi', 1, 'laranja']
try:
    print("Lista l13 original:", l13) 
    l14 = sorted(l13)  # cria uma nova lista ordenada a partir de l13
    print("Nova lista l14 criada com sorted() a partir de l13:", l14)
except TypeError as e:
    print("Erro ao tentar ordenar l13 com diferentes tipos de dados:", e)

print("###################################")

"""
reverse() - inverte a ordem dos elementos da lista in loco (modifica a lista original).
O algoritmo de reverse é mais eficiente que o de sort, pois ele simplesmente inverte a ordem dos elementos, sem precisar compará-los.
"""

l15 = [1,2,3,4,5]
print("Lista l15 original:", l15)
l15.reverse()  # inverte a ordem dos elementos da lista
print("Lista l15 após .reverse():", l15)

l16 = ['a','b','c','d','e']
print("Lista l16 original:", l16)
l16.reverse()  # inverte a ordem dos elementos da lista
print("Lista l16 após .reverse():", l16)    

l17 = ['banana', 'abacaxi', 1, 'laranja']
print("Lista l17 original:", l17)
l17.reverse()  # inverte a ordem dos elementos da lista
print("Lista l17 após .reverse():", l17)

"""
clear() - remove todos os elementos da lista, deixando-a vazia.
"""

l18 = [1,2,3,4,5]
print("Lista l18 original:", l18)
l18.clear()  # remove todos os elementos da lista
print("Lista l18 após .clear():", l18)

print("###################################")

"""
copy() - cria uma cópia rasa (shallow copy) da lista. O motivo é que a atribuição direta cria uma referência à mesma lista na memória.
Modificar valores na variável que recebe a lista afetará a original. Tudo no final das contas é ponteiro.
Complexidade O(n), pois precisa copiar todos os elementos da lista para a nova lista.
"""

l19 = [1,2,3,4,5]
print("Lista l19 original:", l19)

l19_referencia = l19  # cria uma referência à lista l19
l19_referencia.append(6)  # adiciona 6 à lista através da referência
print("Lista l19 após adicionar 6 via referência:", l19)  # l19 também é modificada

l20 = l19.copy()  # cria uma cópia rasa da lista
print("Cópia l20 criada com .copy() a partir de l19:", l20)

"""
listas multidimensionais - listas dentro de listas
"""

l21 = [[1,2,3], [4,5,6], [7,8,9]]  # lista 2D (matriz 3x3)
print("Lista l21 (2D):", l21)
print("Acessando o elemento na linha 1, coluna 2:", l21[1][2])  # acessa o elemento 6

# printando a matriz de forma estruturada
for linha in l21:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # nova linha após cada linha da matriz


"""
deepcopy() - cria uma cópia profunda da lista.

deep copy (cópia profunda) não é necessária para listas simples, mas é importante quando a lista contém outras listas ou objetos mutáveis.

Altamente custoso em matrizes, onde normalmente é usado, pois cria uma nova estrutura de dados na memória, copiando todos os elementos 
recursivamente da matriz. Complexidade O(n*m), onde n é o número de linhas e m é o número de colunas da matriz.
"""
import copy
l22 = [[1,2,3], [4,5,6], [7,8,9]]
l22_referencia = l22  # cria uma referência à lista l22
l22_referencia[0][0] = 'X'  # modifica o elemento na referência
print("Lista l22 após modificar via referência:", l22)  # l22 também é modificada

l22_shallow = l22.copy()  # cria uma cópia rasa da lista
l22_shallow[0][1] = 'Y'  # modifica o elemento na cópia rasa
print("Lista l22 após modificar a cópia rasa:", l22)  # l22 também é modificada, pois a cópia rasa compartilha referências internas

l23 = copy.deepcopy(l22)  # cria uma cópia profunda da lista
print("Cópia l23 criada com deepcopy() a partir de l22:", l23)