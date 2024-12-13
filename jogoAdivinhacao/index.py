import random
import os
erros=0
sorteado=random.randrange(0,1000)
jogador=int(input("Inform your number: "))

while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("FAIL! Number is greater than your guess")
    elif(sorteado<jogador):
        print("FAIL! Number is smaller than your guess")
    erros+=1
    jogador=int(input("Inform your number: "))
print("Number "+str(jogador)+", you win in "+str((erros+1))+" trys")