from random import randint
print('-=' * 12)
print('Sou seu computador...')
print('-=' * 12)
print('''Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = int(input('\033[32mQual é seu palpeite?\033[m '))
computador = randint(1, 10)
tentativa = 1
while jogador != computador:
  if jogador < computador:
    print('Mais... Tente mais uma vez.')
    jogador = int(input('Qual é seu palpite? '))
    tentativa += 1  
  if jogador > computador:
    print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual é seu palpite: '))
    tentativa += 1 
if tentativa == 1:
  print('Acertou com {} tentativa'.format(tentativa))
else:
  print('Acertou com {} tentativas'.format(tentativa))
  


