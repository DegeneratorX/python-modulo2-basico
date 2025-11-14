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
clear() - remove todos os elementos da lista, deixando-a vazia.
"""

l5 = [1,2,3,4,5]
print("Lista l5 original:", l5)
l5.clear()  # remove todos os elementos da lista
print("Lista l5 após .clear():", l5)

print("\n###################################\n")
