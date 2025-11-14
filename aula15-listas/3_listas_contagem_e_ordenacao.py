"""
Contagem e Ordenação em Listas
"""

"""
max() e min() - retornam o maior e o menor valor da lista, respectivamente.
Para listas com strings, ele retorna o maior e o menor valor considerando a ordem alfabética.
Para listas com diferentes tipos de dados, pode gerar erro.
"""

l1 = [91,23,56,38,43,37]

print("Lista l1:", l1)
print("maior:", max(l1))  # Maior valor da lista (inteiro)
print("menor:", min(l1))  # Menor valor da lista (inteiro)
print("###################################")

try: 
    l2 = ['banana', 'abacaxi', 1, 'uva']
    print("Lista l2:", l2)
    print("maior:", max(l2))  # Maior valor da lista (string)
    print("menor:", min(l2))  # Menor valor da lista (string)
except TypeError as e:
    print("Erro ao comparar diferentes tipos de dados na lista:", e)

print("###################################")

"""
range() - cria uma lista de números inteiros em um intervalo determinado.
"""

l3 = range(1,10)  # Função range() do laço for. Percorre 1 até 9.
print(l3)  # Normalmente não acontece nada. Ele simplesmente printa a função.

l3 = list(range(1,10))  # Mas se eu adicionar a função list a função iterável range, eu converto pra lista.
print(l3)  # E com isso não precisa digitar 123...89 dentro de uma lista.

print("###################################")

"""
Estrutura de repetição for com listas
"""

l4 = ['String', True, 10, -20.5]
 
for elemento in l4:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')


print("###################################")

"""
sort() - ordena os elementos da lista in loco (modifica a lista original).
sorted() - retorna uma nova lista ordenada a partir de uma lista existente.
A diferença entre o sorted() e o .sort() é que o sorted() retorna uma nova lista, enquanto o .sort() modifica a lista original.
O algoritmo de sort é mais eficiente que o de sorted, pois o sorted precisa criar uma nova lista na memória.
O algoritmo utilizado para ordenação em ambos os casos é o Timsort, que é uma combinação de Merge Sort e Insertion Sort.
"""

l5 = [5,3,8,1,4]
print("Lista l5 original:", l5) 
l5.sort()  # ordena a lista l5
print("Lista l5 após .sort():", l5)

l6 = [7,2,9,6,0]
print("Lista l6 original:", l6) 
l7 = sorted(l6)  # cria uma nova lista ordenada a partir de l6
print("Lista l6 após sorted():", l6)
print("Nova lista l7 criada com sorted() a partir de l6:", l7) # Mais custoso em termos de memória, mas não modifica a lista original.
l8 = ['banana', 'abacaxi', 'uva', 'laranja']
print("Lista l8 original:", l8) 
l8.sort()  # ordena a lista l8
print("Lista l8 após .sort():", l8)

l9 = ['banana', 'abacaxi', 1, 'laranja']
try:
    print("Lista l9 original:", l9) 
    l10 = sorted(l9)  # cria uma nova lista ordenada a partir de l9
    print("Nova lista l10 criada com sorted() a partir de l9:", l10)
except TypeError as e:
    print("Erro ao tentar ordenar l9 com diferentes tipos de dados:", e)

print("###################################")

"""
reverse() - inverte a ordem dos elementos da lista in loco (modifica a lista original).
O algoritmo de reverse é mais eficiente que o de sort, pois ele simplesmente inverte a ordem dos elementos, sem precisar compará-los.
"""

l11 = [1,2,3,4,5]
print("Lista l11 original:", l11)
l11.reverse()  # inverte a ordem dos elementos da lista
print("Lista l11 após .reverse():", l11)

l12 = ['a','b','c','d','e']
print("Lista l12 original:", l12)
l12.reverse()  # inverte a ordem dos elementos da lista
print("Lista l12 após .reverse():", l12)    

l13 = ['banana', 'abacaxi', 1, 'laranja']
print("Lista l13 original:", l13)
l13.reverse()  # inverte a ordem dos elementos da lista
print("Lista l13 após .reverse():", l13)