"""
Mais exemplos com for
"""

for n in range(0,100,8):  # Esse range é semelhante a linguagem C. N vai de 0 até 100, mas pula 8 casas.
    print(n)  # Por coincidência mostra os múltiplos de 8.

print(" ")

for n in range(100):  # Esse for também mostra todos os múltiplos de 8.
    if n%8 == 0:
        print(n)

print(" ")
##################################

texto = "python"
nova_string = ""

for letra in texto:  # Formação de um novo texto na base do "copia e cola" cada caractere.
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()  # Mesma linha de cima
    else:
        nova_string += letra
print(nova_string)