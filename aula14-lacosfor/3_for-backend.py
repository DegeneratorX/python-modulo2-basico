"""
Iterável: str, range, etc (__iter__)
Iterador: objeto que vai retornar um valor por vez (next)
Iterar: pegar um elemento por vez de um iterável

next: função que retorna o próximo valor do iterador
iter: função que transforma um iterável em um iterador
"""

texto = iter("Python")  # Cria um iterador a partir da string "Python" - __iter__()

print(texto)
print(next(texto))  # Pega o próximo valor do iterador - __next__()
print(next(texto))
print(next(texto))
print(next(texto))

texto_2 = "Victor"
iterador = iter(texto_2)  # Cria um iterador a partir da string "Victor"

"""
Aqui é uma forma manual de iterar sobre o iterador usando while e tratando a exceção StopIteration.
Basicamente é assim que o for funciona por baixo dos panos.
"""
while True:
    try:
        letra = next(iterador)  # Pega o próximo valor do iterador
        print(letra)
    except StopIteration:  # Exceção lançada quando não há mais elementos no iterador
        break