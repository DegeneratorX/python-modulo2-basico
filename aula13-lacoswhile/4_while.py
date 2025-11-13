"""
índices + Whiles
"""
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'  # Valores que possuem índices são chamados iteráveis
tamanho_frase = len(frase)
cont = 0
nova_string = ""  # Atribuo uma string vazia.

while cont < tamanho_frase:
    print(frase[cont], cont)  # Imprime a frase e seu respectivos índices.
    cont += 1
print("")
print("#################")
print("")
####################################

cont = 0
nova_string = ""

while cont < tamanho_frase:
    nova_string += frase[cont]  # "copia e cola" toda a string da variável frase e transfere pra nova_string
    #                             utilizando concatenação.
    print(nova_string)
    cont += 1
