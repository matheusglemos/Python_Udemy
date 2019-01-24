# coding: utf-8

import os

def tabuleiro(jogada):
    print("   |   |   ")
    print(" " + jogada[1] + " | " + jogada[2] + " | " + jogada[3] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + jogada[4] + " | " + jogada[5] + " | " + jogada[6] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + jogada[7] + " | " + jogada[8] + " | " + jogada[9] + " ")
    print("   |   |   ")

def definindo_marcadores():

   marcador = ''

   while not (marcador == 'X' or marcador == 'O'):
      print(" ")
      marcador = str(raw_input(jogador01 + " voce deseja marcar com o X ou com O? ").upper())
      limpar()
      if marcador == 'X':
        print(jogador01 + ' voce marcara com X.')
        print(jogador02 + ' voce marcara com O.')
      else:
        print(jogador01 + ' voce marcara com O.')
        print(jogador02 + ' voce marcara com X.')

   if marcador == 'X':
      return ('X','O')
   else:
      return('O', 'X')

def marcar_no_tabuleiro(jogada,marcador,posicao):

    jogada[posicao] = marcador

def ha_vencedor(jogada,marcador):

    return ((jogada[1] == marcador and jogada[2] == marcador and jogada[3] == marcador) or
            (jogada[4] == marcador and jogada[5] == marcador and jogada[6] == marcador) or
            (jogada[7] == marcador and jogada[8] == marcador and jogada[9] == marcador) or
            (jogada[1] == marcador and jogada[4] == marcador and jogada[7] == marcador) or
            (jogada[2] == marcador and jogada[5] == marcador and jogada[8] == marcador) or
            (jogada[3] == marcador and jogada[6] == marcador and jogada[9] == marcador) or
            (jogada[1] == marcador and jogada[5] == marcador and jogada[9] == marcador) or
            (jogada[3] == marcador and jogada[5] == marcador and jogada[7] == marcador))

import random
def quem_inicia():

    if random.randint(0,1) == 0:
        return jogador01
    else:
        return jogador02

def verifica_espaco(jogada,posicao):

    return jogada[posicao] == ' '

def verifica_se_tabuleiro_esta_completo(jogada):

  for i in range(1,10):
        if verifica_espaco(jogada,i):
            return False

  return True

def posicao_jogada(jogada):

    posicao = " "

    while posicao not in [1,2,3,4,5,6,7,8,9] or not verifica_espaco(jogada,int(posicao)):
        posicao = int(raw_input("Escolha sua jogada (1-9): "))

    return posicao

def jogar_novamente():

    return input('Quer jogar novamente? "S" ou "N"').lower().startswith('s')

def limpar():
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')

print(" ")
print('Bem vindo ao jogo da velha!')
print(" ")

jogador01 = str(raw_input('Jogador(a) 01, por favor digite seu nome: '))
jogador02 = str(raw_input('Jogador(a) 02, por favor digite seu nome: '))

jogos = 0
while True:
    jogada = [' '] * 10
    jogador_01_marcador,jogador_02_marcador = definindo_marcadores()
    turno =  quem_inicia()
    print(" ")
    print ('O(A) jogador(a) ' + turno + ' comecara jogando!')

    game_em_andamento  = True

    while game_em_andamento:
        #jogador 01
        if turno == jogador01:
            print(" ")
            print("Vez de " + jogador01)
            print(" ")
            tabuleiro(jogada)
            print(" ")
            posicao = posicao_jogada(jogada)
            marcar_no_tabuleiro(jogada,jogador_01_marcador,posicao)
            limpar()

        #verifica vitoria
        if ha_vencedor(jogada,jogador_01_marcador):
            tabuleiro(jogada)
            print(" ")
            print('Parabens ' + jogador01 + ', voce venceu! \n')
            break
        else:
            if verifica_se_tabuleiro_esta_completo(jogada):
              tabuleiro(jogada)
              print(" ")
              print("O jogo terminou empatado! \n")
              break
            else:
              turno = jogador02

            #jogador 02
        if turno == jogador02:
            print(" ")
            print("Vez de " + jogador02)
            print(" ")
            tabuleiro(jogada)
            print(" ")
            posicao = posicao_jogada(jogada)
            marcar_no_tabuleiro(jogada,jogador_02_marcador,posicao)
            limpar()

        #verifica vitoria
        if ha_vencedor(jogada,jogador_02_marcador):
            tabuleiro(jogada)
            print(" ")
            print('Parabens ' + jogador02 + ', voce venceu! \n')
            break
        else:
            if verifica_se_tabuleiro_esta_completo(jogada):
                tabuleiro(jogada)
                print(" ")
                print("O jogo terminou empatado! \n")
                break
            else:
                turno = jogador01

    if not jogar_novamente():
        break
