import time

tabuleiro = ['[1]','[2]','[3]',
             '[4]','[5]','[6]',
             '[7]','[8]','[9]']
player = [0,0]
troca = 1

def menu():
    rodar = True
    partida = 0

    #Rodar Partida
    while rodar == True:      
        partida = jogo()

        #Checar quem marcou ponto
        if partida == 1:
            player[0] += 1
        elif partida == 3:
            print('Empate')
        else:
            player[1] += 1 

        #Decidir se quer continuar ou parar      
        print(f'Player1: {player[0]} | Player2: {player[1]}')
        reset = input('Revanche? [S/N] ').upper().strip()[0]
        while reset not in 'SN':
            reset = input('Entrada Inválida. Revanche? [S/N] ').upper().strip()[0]
        rodar = True if reset == 'S' else False

        #Trocar O Jogador que começa
        global troca
        if troca == 1:
            troca += 1
        else:
            troca -= 1
        
        #Resetar Tabuleiro
        for i in range(9):
            tabuleiro[i] = f'[{i+1}]'
    
    #Finalizar Mostrando Resultados
    if player[0] > player[1]:
        print(f'Player1 ganhou de {player[0]} a {player[1]}')
    elif player[0] == player[1]:
        print('Terminou Empatado')
    else:
        print(f'Player2 ganhou de {player[1]} a {player[0]}')

    time.sleep(5)

def jogo():
    global troca
    player = troca
    fim = False
    rodada = 0
    while fim == False:
        gerar_tabuleiro()

        #Player 1
        if player == 1 and fim == False:
            jogada('[X]', player)
            fim = checkup('[X]')
            player = 2 if not fim else 1
            rodada += 1

        #Player2
        elif player == 2 and fim == False:
            jogada('[O]', player)
            fim = checkup('[O]')
            player = 1 if not fim else 2
            rodada += 1
        
        #Checar Empate
        if rodada == 9:
            fim = True

    #Finalização
    gerar_tabuleiro()
    if rodada != 9:
        return player
    else:
        return 3
    
def jogada(peça, i):
    posicao = int(input(f'Escolha uma posição Jogador {i}: '))
    while f'[{posicao}]' not in tabuleiro:
        posicao = int(input(f'Posiçao Invalida. Escolha uma posição Jogador {i}: '))
    tabuleiro[posicao-1] = peça

def checkup(peça):
    lista = [peça,peça,peça]
    #Checar Horizontal
    for i in range(0,7,3):
        if tabuleiro[i:i+3] == lista:
            return True
        
    #Checar Vertical
    for i in range(3):
        linha = []
        for x in range(0,9,3):
            linha.append(tabuleiro[i+x]) 
        if linha == lista:
            return True
        else:
            linha = []
    
    #Checar em X
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == peça:
        return True
    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == peça:
        return True
    else:
        return False

def gerar_tabuleiro():
    print('='*9)   
    for i,bloco in enumerate(tabuleiro):
        if (i+1) % 3 == 0:
            print(bloco)
        else:
            print(bloco,end='')
    print('='*9)   
    
if __name__ == "__main__":
    menu()
