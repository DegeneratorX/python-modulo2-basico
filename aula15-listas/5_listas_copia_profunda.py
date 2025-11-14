"""
deepcopy() - cria uma cópia profunda da lista.

deep copy (cópia profunda) não é necessária para listas simples, mas é importante quando a lista contém outras listas ou objetos mutáveis.

Altamente custoso em matrizes, onde normalmente é usado, pois cria uma nova estrutura de dados na memória, copiando todos os elementos 
recursivamente da matriz. Complexidade O(n*m), onde n é o número de linhas e m é o número de colunas da matriz.
"""

import copy

l1 = [[1,2,3], [4,5,6], [7,8,9]]
l1_referencia = l1  # cria uma referência à lista l1
l1_referencia[0][0] = 'X'  # modifica o elemento na referência
print("Lista l1 após modificar via referência:", l1)  # l1 também é modificada

l1_shallow = l1.copy()  # cria uma cópia rasa da lista
l1_shallow[0][1] = 'Y'  # modifica o elemento na cópia rasa
print("Lista l1 após modificar a cópia rasa:", l1)  # l1 também é modificada, pois a cópia rasa compartilha referências internas

l1_deep = copy.deepcopy(l1)  # cria uma cópia profunda da lista
print("Cópia l1_deep criada com deepcopy() a partir de l1:", l1_deep)