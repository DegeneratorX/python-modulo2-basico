import re

def main():
    while True:
        entrada = input("Digite um CPF: ")
        cpf_usuario_str = re.sub(r'[^0-9]', "", entrada)

        entrada_eh_sequencial = entrada == entrada[0] * len(entrada)

        if entrada_eh_sequencial:
            print("Vocễ enviou dados sequenciais.")
            continue

        nove_digitos = cpf_usuario_str[:9]
        count_1 = 10
        res_digito_1 = 0

        for dig in nove_digitos:
            res_digito_1 += int(dig) * count_1
            count_1 -= 1
        
        digito_1 = (res_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        ###############################

        dez_digitos = nove_digitos + str(digito_1)
        count_2 = 11
        res_digito_2 = 0

        for digito in dez_digitos:
            res_digito_2 += int(digito) * count_2
            count_2 -= 1
        digito_2 = (res_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        ###############################

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        if cpf_usuario_str == cpf_gerado_pelo_calculo:
            print(f"{cpf_usuario_str} é válido.")
        else:
            print("CPF Inválido.")


if __name__ == '__main__':
    main()