"""
Condições IF, ELIF (else if) e ELSE em Python
"""
a = True
if a:
    print("Verdadeiro.")

if not a:
    print("Olá")
# Olá não foi impresso


if True:
    print("True2")
else:
    print("Nunca será impresso")

if False:
    print("Nunca será impresso")
elif True:
    print("True3")
else:
    print("Nunca será impresso")

# Exemplo mais complexo
entrada = input("Você quer entrar ou sair? ")
if entrada == "entrar":
    print("Você entrou no sistema.")
elif entrada == "sair":
    print("Você saiu do sistema.")
else:
    print("Comando não reconhecido.")

