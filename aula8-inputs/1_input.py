"""
Entrada de dados. 
A função input() permite a entrada de dados pelo usuário via teclado.
Por padrão, o input() sempre retorna uma string.
Se for necessário outro tipo de dado, é preciso fazer a conversão explícita.
Exemplo: int(), float(), bool()
"""

nome = input("Qual o seu nome? ")  # atribui um valor de input nessa variavel 'nome'.
print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')

# Sempre nesse caso será str, mesmo digitando 10, será reconhecido como string.

idade = input("Qual a sua idade? ")



# Pra usar inteiro da string do input da idade, é necessário converter a string em int.

ano_nascimento = 2022-int(idade)  # Assim posso fazer a subtração

print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}.')

# convertendo direto na atribuição NÃO é uma boa prática, mas funciona.
peso = float(input('Digite seu peso em kg: '))  
print(peso, type(peso))
# O motivo é que dificulta o debug, caso dê erro na conversão (por exemplo, digitando letras ao invés de números)
# O ideal é fazer a conversão em uma linha separada, para facilitar a identificação do erro.

