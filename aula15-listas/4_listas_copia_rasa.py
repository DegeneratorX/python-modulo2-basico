"""
copy() - cria uma cópia rasa (shallow copy) da lista. O motivo é que a atribuição direta cria uma referência à mesma lista na memória.
Modificar valores na variável que recebe a lista afetará a original. Tudo no final das contas é ponteiro.
Complexidade O(n), pois precisa copiar todos os elementos da lista para a nova lista.
"""

l1 = [1,2,3,4,5]
print("Lista l1 original:", l1)

l1_referencia = l1  # cria uma referência à lista l1
l1_referencia.append(6)  # adiciona 6 à lista através da referência
print("Lista l1 após adicionar 6 via referência:", l1)  # l1 também é modificada

l2 = l1.copy()  # cria uma cópia rasa da lista
print("Cópia l2 criada com .copy() a partir de l1:", l2)