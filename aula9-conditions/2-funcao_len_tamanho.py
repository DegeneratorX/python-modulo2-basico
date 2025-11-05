"""
Condição com a função len() para verificar o tamanho de uma string em Python
"""

usuario = input("Digite seu usuário: ")

qtd_caracteres = len(usuario) # Função len() retorna a quantidade de caracteres da string

print(usuario, qtd_caracteres, type(qtd_caracteres)) # Exibe o usuário, a quantidade de caracteres e o tipo da variável qtd_caracteres


# Condição para verificar se a quantidade de caracteres é menor que 6
if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")

###########################################

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

# Soma de caracteres das duas strings
print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")

# Não funciona com números nem boolean. É necessário converter.
numero = int(input("Digite um número: ")) # Digite 135 por exemplo

print(len(str(numero))) # Se não converter para string, dá erro. Aqui convertemos para str antes de usar len().
