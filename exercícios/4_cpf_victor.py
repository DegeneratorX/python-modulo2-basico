"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

#################################################

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

"""

def main():
    loop = True
    while loop:
        cpf_usuario_str = input("Digite um CPF: ")
        cpf_usuario_str = cpf_usuario_str.replace(".","") \
            .replace(" ", "") \
            .replace("-","") \
            .strip()
        
        lista_cpf_usuario_str = list(cpf_usuario_str)

        cpf_int = []
        for fatia in lista_cpf_usuario_str:
            for dig in fatia:
                cpf_int.append(int(dig))

        for indices_ultimos_digitos in range(9, 11):

            count = indices_ultimos_digitos + 1
            soma = 0

            for dig in range(indices_ultimos_digitos):
                res_multiplicacao = cpf_int[dig] * count
                soma = soma + res_multiplicacao
                count -= 1
            mult_final = soma * 10
            resto_final = mult_final % 11

            if resto_final > 9:
                digito_final_para_comparar = 0
            else:
                digito_final_para_comparar = resto_final

            if indices_ultimos_digitos == 9 and digito_final_para_comparar == cpf_int[9]:
                print("Primeiro Dígito Válido:", digito_final_para_comparar)
            elif indices_ultimos_digitos == 10 and digito_final_para_comparar == cpf_int[10]:
                print("Segundo Dígito Válido:", digito_final_para_comparar)
            else:
                print("CPF inválido em um dos dígitos")


if __name__ == '__main__':
    main()