num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

try:  # Tenta executar esse código. Se não der certo...
    num1 = float(num1)
    num2 = float(num2)

    print(num1+num2)
except:  # Executa esse aqui. Esse cara executa quando o console dá erro nesse try.
    print("ERRO") 
