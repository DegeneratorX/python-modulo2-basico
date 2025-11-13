titulo = "BeM viNdO"

print(titulo.lower())  # Deixa tudo minúsculo
print(titulo.upper())  # Deixa tudo maiúsculo
print(titulo.title())  # Primeira letra maiúsculas de cada palavra
print(titulo.capitalize())  # Primeira letra maiúscula da string

print(f'{titulo:=^20}') # Adiciona = ao centro, totalizando 20 caracteres

str_exemplo = "ABC"

print(f'{str_exemplo: >10}')  # Adiciona espaços à esquerda, totalizando 10 caracteres
print(f'{str_exemplo:.<10}')  # Adiciona . à direita, totalizando 10 caracteres
print(f'{str_exemplo:-^10}')  # Adiciona - ao centro, totalizando 10 caracteres


print("\n#############################################\n")

print("######## CONVERSION FLAGS ########\n")
"""
Conversion Flags:

- !r : Representação oficial da string (útil para depuração)
- !s : Representação informal da string (padrão)
- !a : Representação com caracteres ASCII (útil para strings com caracteres especiais)

Basicamente são usadas para converter o valor antes de formatá-lo. Exemplos:

- !r : chama repr()
- !s : chama str()
- !a : chama ascii()

"""
print(f'{str_exemplo!r}') # Representação oficial da string (útil para depuração)
print(f'{str_exemplo!s}') # Representação informal da string (padrão)
print(f'{str_exemplo!a}') # Representação com caracteres ASCII (útil para strings com caracteres especiais)