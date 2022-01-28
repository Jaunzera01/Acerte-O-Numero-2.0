#Base e biblioteca:
from random import randint
IA = randint(0, 20)
print('Tente adinhivar o número na minha mente')
acertou = False
ideia = 0

#Ideias e erros:
while not acertou:
    jogador = int(input('Alguma ideia?'))
    ideia += 1
    if jogador == IA:
        acertou = True
    else:
        if jogador < IA:
            print('Mais... tente novamente.')
        elif jogador > IA:
            print('Menos... tente de novo.')

#Parabéns:
            print('Você acertou com {} tentativas. Muito bem!'.format(ideia))