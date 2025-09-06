#jogo de adivinhação
#autores: Paulo Vilela, Vinícius Henrique
# Data: 29/05/2025

import os 
#entrada
while True:
    jogador1 = int(input('Digite um número de 1 a 10:'))
    if 1 <= jogador1 <= 10:
        break
    else:
        print('Número inválido! Digite um número entre 1 e 10.')

tentativas = 0

#limpa a tela
os.system('cls')
#contador
while True:
    jogador2 = int(input('Adivinhe o número de 1 a 10 que o Jogador n°1 digitou:')) 
    tentativas+=1
    if jogador2 == jogador1:
        print(f'Parabens, você acertou o número {jogador1} em {tentativas} tentativas!')
        break
    else:
        print('Você errou, tente novamente!')
    

    

        