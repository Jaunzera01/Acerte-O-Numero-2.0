#Biblioteca:
import random
def gera():
    return random.randint(0,25)

#Jogo:
numeroaleatorio = gera()
print('Tente adivinhar um número aleatório de 0 à 25, a maioria das pessoas acertam com 5 tentativas!')
jogada = int(input('Qual a sua ideia?: '))
cont = 1

def game():
    resposta = gera()
    tentativa = 10
while jogada != numeroaleatorio:
    if jogada > numeroaleatorio:
        print('Uh, foi quase, tente um número menor...')
    elif jogada < numeroaleatorio:
        print('Uh, foi quase, tente um número maior...')
    jogada = int(input('Tente novamente: '))
    cont += 1

print("Parabéns, você venceu com {} tentativas!!!".format(cont))
while True:
    game()
