"""
Tuplas - mesma coisa da lista, só não é modificável.
Sempre entre parênteses (ou sem parênteses também, mas somente 2 ou mais elementos!).
Se sem parênteses e 1 elemento, será int, str, float etc...
"""

t1 = (1, 2, 3, 'Victor')
t2 = (1,)  # Exceção: Com parênteses, botando
t3 = 1, 2, 3, 'Victor'  # Mesma coisa de 't1 = (1,2,3,'Victor')'
t4 = 1,  # Exceção: Sem parênteses, botando 1 vírgula, 1 elemento definido vira tupla.
print("Tipo do t1, t2, t3, t4:", type(t1), type(t2), type(t3), type(t4))
print("Print do t3:", t3)
print("Print do t3[1]:", t3[1])

"""
Mofificando tuplas

Tuplas são imutáveis, ou seja, não podem ser modificadas. Porém, podemos convertê-las em listas, modificar e voltar a ser tupla.
Não é recomendado fazer isso, pois perde-se a ideia de tupla (imutabilidade). Apenas para casos específicos, pois a imutabilidade
avisa, pela boa prática de um programador para outro, que aquele conjunto de dados no código não deve ser modificado.
"""

t5 = list((1,2,3,4,5))  # Conversão de tupla em lista. Agora posso editar os valores.
t5[1] = 3000  # Provando que consegui alterar o valor da "tupla" (lista)
tuple(t5)  # Conversão de lista em tupla. Voltando ao estado inicial.
print("Print do t5:", t5)