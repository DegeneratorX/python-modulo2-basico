"""
Enumerate - Enumerar elementos da lista # iteráveis
"""

# Seja o segunte exemplo:

lista = ['Maria', 'João', 'Luiz', 'Ana']

for indice in range(len(lista)):  # len() pega o tamanho da lista
    print(indice, lista[indice])  # índice = 0,1,2... lista[indice] = valor dentro da lista.


print("\n################################\n")

"""
É possível replicar isso com a função enumerate(), que já faz isso internamente:
"""

lista_enumerada = enumerate(lista)  # Cria um objeto enumerate
print(lista_enumerada, type(lista_enumerada))  # Mostra que é um objeto enumerate, e é um iterador.
print(next(lista_enumerada))  # Mostra o próximo elemento do iterador.
print(next(lista_enumerada))  # Mostra o próximo elemento do iterador.
# E assim vai...

# Exemplo definitivo de uso:
for indice, valor in enumerate(lista):  # indice = 0,1,2... valor = valor dentro da lista.
    print(indice, valor, lista[indice])  # valor e lista[indice] são exatamente iguais. Enumerate é uma alternativa.

#############################################

# É possível também converter o enumerate em uma lista:
lista_enumerada = list(enumerate(lista))
print("Conversão de enumerate para list:", lista_enumerada)  # Mostra a lista enumerada como lista de tuplas.
# Nessa conversão ele também converte de um iterador para um iterável (lista).