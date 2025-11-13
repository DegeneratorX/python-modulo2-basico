"""
While / Else
contadores
acumuladores

- Contadores: Variáveis que vão contando quantas vezes uma ação foi realizada.
- Acumuladores: Variáveis que vão acumulando valores ao longo do tempo.

O else é um bloco de código que é executado quando a condição do while se torna falsa.
Parece inútil, mas tem sua utilidade quando usamos break dentro do while. Se o
break for executado, o else não será executado.

"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

###############################

# Exemplo com break no while e else
while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:  # Esse else tem utilidade na seguinte situação: quando tem break no while, o else não é lido.
    print("Cheguei no else. Por conta do 'break', não serei executado.")
print("Mas isso aqui sim será executado.")
