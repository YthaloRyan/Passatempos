from string import ascii_lowercase
import getpass

#Palavra Para o Jogo
palavra = getpass.getpass('Insira a palavra ou frase para o jogo: ').lower().strip()
palavra_final = []
alfabeto = ascii_lowercase
count = 0

#Receber numero de vidas
vida = input('Quantas vidas você deseja ? ')
while not vida.isnumeric():
    vida = input('Entrada Invalida. Quantas vidas você deseja ? ')
vida = int(vida)

#Esconder palavra
for i in palavra:
    if i == ' ':
        palavra_final.append(' ')
    else:
        palavra_final.append('_')

#Rodar Jogo
while True:
    #Receber entrada do jogador
    print('='*55)
    print(f'Você tem {vida} tentativa(s).')
    print(alfabeto)
    tentativa = input(f'{"".join(palavra_final)} Insira uma letra: ').lower().strip()
    while len(tentativa) != 1 or tentativa not in alfabeto:
        if tentativa not in alfabeto:
            tentativa = input(f'Esta letra já foi usada. {"".join(palavra_final)} Insira outra letra: ').lower().strip()
        else:
            tentativa = input(f'Entrada Incorreta {"".join(palavra_final)} Insira uma letra: ').lower().strip()
    alfabeto = alfabeto.replace(tentativa,'')
    count += 1

    #Checar se a entrada faz parte da palavra
    if tentativa in palavra:
        for pos,char in enumerate(palavra):
            if char == tentativa:
                palavra_final[pos] = tentativa
    else:
        vida -= 1
    print('='*55)
    print(f'Você tem mais {vida} tentativa(s).')

    #Checar se morreu
    if vida == 0:
        print('='*55)
        print(f'Uma Pena Você Perdeu, a palavra era [{palavra}].')
        print(f'Você tentou {count} vez(es).')
        print('='*55)
        break
    
    #Checar se o jogador ganhou
    if '_' not in palavra_final:
        print('='*55)
        print(f'Parabéns Você Ganhou, a palavra era [{palavra}].')
        print(f'Foram necessário {count} tentativas.')
        print(f'Sobraram {vida} vida(s).')
        print('='*55)
        break
