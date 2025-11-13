"""
While

- São estruturas de repetição que repetem um bloco de código enquanto uma condição for verdadeira.
"""

x = 0

# Enquanto x for menor que 5, faça:
while x < 5:
    print(x)
    x += 1  # x = x + 1

print("Acabou!")

#################################

# Exemplo com continue
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # Tudo daqui pra baixo não será executado mais enquanto estiver dentro do While. Ele irá pro proximo passo
    # looping.
    print(x)
    x = x + 1

##################################

# Exemplo com break
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # Força o python a sair do looping.
    print(x)
    x = x + 1

###################################

# Exemplo de while aninhado
x = 0 # coluna

while x < 10:
    y = 0  # linha
    
    while y < 5:
        print(f"x vale {x} e y vale {y}.")
        y += 1

    x += 1 # x = x + 1

###################################

