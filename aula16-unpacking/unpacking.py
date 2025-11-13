"""
Desempacotamento de listas
"""
lista = ['Luiz', 'João', 'Maria']

n0, n1, n2 = lista  # Desempacotamento

print("Valor de n1 da lista:", n1)

#########################################

lista2 = ['Luiz', 'João', 'Maria', 'Generico', 1, 2, 3, 4, 8]

b0, b1, b2, *b3 = lista2  # O asterisco gera outra lista ao desempacotar.

print("Valores dos desempacotamentos:", b0, b1, b2, b3)  # Tudo após o asterisco serão os últimos números.

c0, c1, c2, *c3, c4 = lista2

print("Valores dos desempacotamentos:", c0, c1, c2, c3, c4)  # Tudo após o asterisco serão os últimos números.

#########################################

lista3 = ['Luiz', 'João', 'Maria', 'Generico']

d0, d1, d2, d3, *resto = lista3
print("Valores dos desempacotamentos:", d0, d1, d2, d3, resto)  # Resto será uma lista vazia.