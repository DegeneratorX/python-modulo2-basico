usuario = input("Digite seu usuário: ")

qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")

###########################################

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")
# Soma de caracteres

# Não funciona com números nem boolean. É necessário converter.

numero = input("Digite um número: ")

print(len(str(string1)))
