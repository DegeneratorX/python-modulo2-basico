"""
lacoswhile

Exercício calculadora simples
"""
while True:
    print()
    num1 = input("Digite um numero:  ")
    num2 = input("Digte outro numero: ")
    operador = input("Digite o operador: ")


    """
    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número')
        continue
    """

    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print("Erro: valores digitados não são números.")
        continue


#   - + * /

    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 + num2)
    elif operador == "*":
        print(num1 * num2)
    elif operador == "/":
        print(num1 / num2)
    else:
        print("Operador inválido!")

    sair = input("Deseja sair? [s]im ou [n]ão: ")
    if sair == "s":
        break
