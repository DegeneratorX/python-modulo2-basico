"""
Listas em Python

Exercício - Jogo da Forca
"""
secreto = 'perfume'  # Palavra secreta
digitadas = []  # Crio uma string vazia
chances = 3  # Dou 3 chances ao usuário

while True:  # Crio um looping infinito até o jogo acabar com o Break.
    if chances <= 0:  # Se acabar as chances, sai do jogo.
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')  # Usuário irá digitar uma letra.

    if len(letra) > 1 or letra.isdigit():  # Se a letra for um número ou tiver mais de dois caracteres, retorna o loop.
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue  # Retorna o loop.

    digitadas.append(letra)  # Adiciona a letra na lista vazia.

    if letra in secreto:  # Se a letra digitada está na palavra...
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()  # Como a letra digitada não pertence a palavra a descobrir, imediatamente retira ela da lista.

    secreto_temporario = ''  # String temporária para armazenar letras e asteriscos.
    for letra_secreta in secreto:  # Percorre toda a palavra 'secreto'.
        if letra_secreta in digitadas:  # Verifica se a letra p, e, r... está nas que já foram inseridas na lista.
            secreto_temporario += letra_secreta  # Se sim, então a letra é "relevada".
        else:
            secreto_temporario += '*'  # Se não, ela fica oculta com asterisco até aparecer o dígito correto.

    if secreto_temporario == secreto:  # Se no final das contas os asteriscos não aparecerem...
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')  # Significa que achou todas as letras.
        break
    else:  # Mostra como está a palavra com asteriscos ocultando.
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:  # Se a letra digitada não pertence à palavra, diminui uma chance do usuário.
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
