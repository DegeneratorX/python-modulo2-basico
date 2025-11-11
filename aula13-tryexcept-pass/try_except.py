"""
As vezes você quer fazer um cálculo numa calculadora e é impossível, pois você digita a letra A, e o compilador acusa
de erro. Por exemplo, dentro do input() você quer somar 2 números, e você digita A e 2. O python vai acusar de erro,
pois é impossível converter A pra inteiro. Pra resolver isso, segue abaixo.
"""

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

# isnumeric = isdigit = isdecimal
# checa se tem só números e positivos

print(num1.isnumeric())  # Acusará false se tiver o traço negativo ou ponto flutuante.
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():  # se num1 e num2 são numéricos, é válido converter.
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:  # se não, erro. Pra prevenir erro vermelho de console.
    print("Não pude converter os números para realizar a conta.")

# Infelizmente esse método não resolve o problema de float + int. No próximo arquivo terá uma solução.
