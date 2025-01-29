import time

def exibeUmaCartela(cartela):
    count=0
    for val in cartela:
        print("%-2d"%val,end=" ")
        count+=1
        if count==8:
            print("")
            count=0
           
           
def geraCartelas():
    lCartelas = [[], [], [], [], [], []]
    lPotencias = [1, 2, 4, 8, 16, 32]
    for n in range(1, 64):
        valor = n
        for pos in range(5,-1,-1):
            if valor >= lPotencias[pos]:
                lCartelas[pos].append(n)
                valor -= lPotencias[pos]
    return lCartelas

def exibeMensagemInicial():
    print("*************************************************************")
    print("*                      Jogo da adivinhação                  *")
    print("* Pense em um inteiro de 1 a 63 e não conte pra ninguém!    *")
    print("* Em seguida, tecle ENTER para continuar... e boa sorte!    *")
    print("*                                                           *")
    print("*************************************************************")
    input()

exibeMensagemInicial()
lCart = geraCartelas()
numero_adivinhado = 0
for i, cartela in enumerate(lCart):
     exibeUmaCartela(cartela)
     resp = input("O número que você pensou está nessa cartela? <s/n> ")
     print("")
     if resp.lower() == 's':
         numero_adivinhado += (2**i)

print ('O número escolhido foi.....', end = "") 
time.sleep(2)
print(f'{numero_adivinhado}!')
