import math

"Algumas conta no codigo ja estão sendo 'puladas'"

TamCache=0
ConjMap = 10
TamBloco = 4 ###igual a 16 bytes == 2^4
PolitSub= 3
TamMem = 32
mapeamento = ""

def inicio(tCache,map,subst):

    print("=-="*30)
    print("Escolha o Tamanho da cache :\n1º 1KB\n2º 2KB\n3º 4KB\n4º 8KB\n5º 16KB \n")
    escolha1=6
    while(escolha1 > 5 or escolha1 < 1):
        escolha1=int(input("Escolha : "))
    if (escolha1 == 1):
        tCache=10
    elif(escolha1==2):
        tCache=11
    elif(escolha1==3):
        tCache=12
    elif(escolha1==4):
        tCache=13
    elif(escolha1==5):
        tCache=14 
    print("=-="*30)
    print("Escolha o tipo de mapeamento :\n1º Direto\n2º 2-way\n3º 4-way\n4º 8-way\n")
    escolha2=5
    while(escolha2 > 4 or escolha2 < 1):
        escolha2=int(input("Escolha : "))
    if (escolha2 == 1):
        map = "Direto"
        Nmap = 0
    elif(escolha2 == 2):
        map = "2-way"
        Nmap = 1
    elif(escolha2 == 3):
        map = "4-way"
        Nmap = 2
    elif(escolha2 == 4):
        map = "8-way"
        Nmap = 3
    print("=-="*30)
    escolha3=3
    print("Escolha a Politica de Substituição :\n1º LRU\n2º FIFO\n")
    while(escolha3<1 or escolha3>2):
        escolha3=int(input("Escolha: "))
    if (escolha3 == 1):
        subst = "LRU"
    else:
        subst= "FIFO"
    print("=-="*30)
    
    
    return(tCache,Nmap,subst,map)

def calculos(tamBloco,tamCache,tipoMap):
    numLinhasCache = tamCache-tamBloco
    TamConj = tamBloco+tipoMap
    NumConj = tamCache - TamConj
    index = numLinhasCache
    offSet = NumConj
    Tag = 32-(index+offSet)
    print("A tag tem {} bits, index tem {} bits, offset tem {} bits.".format(Tag,offSet,index))
    print("=-="*30)
    


tamCache,ConjMap,PolitSub,mapeamento=inicio(TamCache,ConjMap,PolitSub)
print('Tamanho da Cache : 2^{}, Mapeamento : {} e Politca de Substituição : {}'.format(tamCache,mapeamento,PolitSub))
print("=-="*30)
calculos(TamBloco,tamCache,ConjMap,)









