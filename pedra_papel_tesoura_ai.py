from random import randint

rand_num = randint(0,2)

name = input('Digite seu nome, jogador -> ')
if name == '':
    name = input('Digite um nome válido, jogador -> ')
    if name == '':
        print('Você não sabe brincar?')
else:
    player = input('Qual você escolhe? Pedra, papel ou tesoura -> ').lower()
    if rand_num == 0:
        computer = 'pedra'
    elif rand_num == 1:
        computer = 'papel'
    else: 
        computer = 'tesoura'

    if player == computer:
            print('Deu empate! ' + name + ' escolheu: ' + player + ' e o computador escolheu: ' + computer)
    if computer == 'pedra':
        if computer == 'tesoura':
            print(name + ' venceu, pois escolheu: ' + player)
            print('computer perdeu, pois escolheu: ' + computer)
        elif computer == 'papel':
            print('computer venceu, pois escolheu: ' + computer)
            print(name + ' perdeu, pois escolheu: ' + player)
    if player == 'papel':
        if computer == 'tesoura':
            print('computer venceu, pois escolheu: ' + computer)
            print(name + ' perdeu, pois escolheu: ' + player)
        elif computer == 'pedra':
            print(name + ' venceu, pois escolheu: ' + player)
            print('computer perdeu, pois escolheu: ' + computer)
    if player == 'tesoura':
        if computer == 'pedra':
            print('computer venceu, pois escolheu: ' + computer)
            print(name + ' perdeu, pois escolheu: ' + player)
        elif computer == 'papel':
            print(name + ' venceu, pois escolheu: ' + player)
            print('computer perdeu, pois escolheu: ' + computer)
    else:
        'Alguma coisa deu errada'