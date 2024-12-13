import os
import random
from colorama import Fore, Back, Style

jogarNovamente="s"
jogadas=0
vitorias=0
empates=0
derrotas=0
quemJoga=2 #1=cpu - 2=jogador
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]
def tela():
    global velha, jogadas, vitorias, empates, derrotas
    os.system("cls")
    print("    0   1   2")
    
    for i in range(3):
        print(f"{i}:  {velha[i][0]} | {velha[i][1]} | {velha[i][2]}")
        if i < 2:  # Evita a linha de separação após a última linha
            print("   -----------")
    
    print(f"Jogadas:-------------"+Fore.BLUE + str(jogadas) + Fore.RESET)
    print(f"Vitórias do Jogador:-"+Fore.GREEN + str(vitorias)+Fore.RESET)
    print(f"Empates do Jogador:--"+Fore.YELLOW + str(empates)+Fore.RESET)
    print(f"Derrotas do Jogador:-"+Fore.RED + str(derrotas)+Fore.RESET)
def jogadorJoga():
    global jogadas; quemJoga; vitorias; derrotas; empates;maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        try:
            l=int(input("Linha..: "))
            c=int(input("Coluna.:"))
            while velha[l][c]!=" ":
                l=int(input("Linha..: "))
                c=int(input("Coluna.:"))
            velha[l][c]=Fore.BLUE+"X"
            quemJoga=1
            jogadas+=1
        except:
            print("Jogada invalida")
            os.system("pause")
def cpuJoga():
    global jogadas; quemJoga; vitorias; derrotas; empates;maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!=" ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]=Fore.RED+"O"
        quemJoga=2
        jogadas+=1
def verificaraVitoria():
    global velha
    vitoria="n"
    simbolo=["X","O"]
    for s in simbolo:
        vitoria="n"
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="n"):
            break
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        soma=0
        idiag=0
        while idiag<3:
            if(velha[idiag][idiag]==s):
                    soma+=1
        if(soma==3):
                vitoria=s
                break
        idiagl=0
        idiagc=2
        while idiagc>=0:
            if(velha[idiagl][idiagc]==s):
                soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
                vitoria=s
                break
    return vitoria
def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=2
    maxJogadas=9
    vit="n"
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
    ]
while(jogarNovamente=s):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificaraVitoria()
        if((vit!="n")or(jogadas>=maxJogadas)):

        print(Fore.RED +"FIM DE JOGO"+ Fore.YELLOW)
        if(vit=="X" or vit=="O"):
            if(vit=="X"):
                ganhador="Jogador"
                vitorias+=1
            elif(vit=="O"):
                ganhador="PC"
                derrotas+=1
        else:
            print("Partida resultou em empate")
            empates+=1
#tempo video 13h18
