"""
O nome das variáveis deve iniciar com letra, pode conter números, separar _, letras minúsculas e maiúsculas (case sensitive)
Não pode usar palavras reservadas (def, for, if, else, import, from, as, etc)
Evitar usar acentos e caracteres especiais (ç, ã, á, é, etc)
Evitar usar letras maiúsculas no início (padrão da comunidade é minúsculo)
Constantes são convencionalmente escritas completamente em maiúsculas (ex: VALOR_PI = 3.14)
"""

nome = 'Victor'
idade = 25
altura = 1.83
e_maior = idade > 18  # se idade for maior que 18, retorna true
peso = 110

print(nome, type(nome))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É de maior:', e_maior)

print('IMC:', peso/(altura**2))

imc = peso/(altura**2)

print(nome, 'tem', idade, 'de idade,', 'possui', altura, 'de altura,', 'pesa', peso, 'kg', 'e tem IMC', imc)