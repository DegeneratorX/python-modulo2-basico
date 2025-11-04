"""
str - string
"""

print('Essa é uma string')  # string, as aspas.
print("Também é, mas em aspas duplas")  # também pode usar duplas
print(123456)  # não é string, o python detecta isso (tipagem dinâmica).

# tudo que estiver em aspas, é ‘string’, incluindo a documentação de aspas tripla.

print("Essa é uma 'string' (str)")  # Colocar aspas simples dentro de uma dupla funciona.
# Colocar uma simples dentro de outra simples não funciona. Por isso existem dois tipos de aspas para string.
# Mas existe outra forma de fazer isso:
print('Essa é uma \'string\' (str)')  # Colocar a barra invertida antes da aspa simples, avisa ao python que aquela aspa é parte da string.

print(r'Esse é meu \n texto (str)')  # colocar "r" antes da string avisa ao compilador que tudo que estiver dentro,
# não pode ser executado como código, por exemplo, \n, que significa quebra de linha.

# Por fim, isso aqui é considerado string:
print("""Essa é uma string com aspas triplas.
Ela pode ocupar várias linhas sem problemas.
""")

# E isso aqui também é uma string:
"""Esse é outro exemplo de string com aspas triplas.
Ela também pode ocupar várias linhas sem problemas.
Funciona como comentário (mas não é) e é utilizada para fazer Docstring.
Se não for a primeira instrução (antes de função, classe ou módulo), não tem efeito em tempo de execução.
Ainda assim, é uma string literal e é compilada e ocupa memória (constantes do código) e vai para o .pyc.
""" # string de aspas triplas não atribuída a variável.