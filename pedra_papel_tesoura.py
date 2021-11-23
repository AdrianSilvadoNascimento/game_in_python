print('Pedra\npapel\ne\ntesoura...')

name1 = input('Digite o nome do primeiro jogador -> ')
name2 = input('Digite o nome do segundo jogador -> ')

if name2 == name1:
    name2 = input('Digite um nome diferente do primeiro jogador, ou adicione sobrenome -> ')
    if name2 != name1:
        p1 = input(name1 + ', qual você escolhe ? -> pedra, papel ou tesoura? ')
        print('**SEM VER O DO ADVERSÁRIO**\n\n' * 20)
        p2 = input(name2 + ', qual você escolhe? -> pedra, papel ou tesoura? ')

if p1 and p2:
    if p1 == p2:
        print('Empate')
    elif p1 == 'pedra':
        if p2 == 'tesoura':
            print(name1 + ' venceu, pois escolheu: ' + p1)
            print(name2 + ' perdeu, pois escolheu: ' + p2)
        elif p2 == 'papel':
            print(name2 + ' venceu, pois escolheu: ' + p2)
            print(name1 + ' perdeu, pois escolheu: ' + p1)
    elif p1 == 'papel':
        if p2 == 'tesoura':
            print(name2 + ' venceu, pois escolheu: ' + p2)
            print(name1 + ' perdeu, pois escolheu: ' + p1)
        elif p2 == 'pedra':
            print(name1 + ' venceu, pois escolheu: ' + p1)
            print(name2 + ' perdeu, pois escolheu: ' + p2)
    elif p1 == 'tesoura':
        if p2 == 'pedra':
            print(name2 + ' venceu, pois escolheu: ' + p2)
            print(name1 + ' perdeu, pois escolheu: ' + p1)
        elif p2 == 'papel':
            print(name1 + ' venceu, pois escolheu: ' + p1)
            print(name2 + ' perdeu, pois escolheu: ' + p2)
else:
    print('Alguma coisa deu errado')