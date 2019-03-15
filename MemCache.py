import math

"Algumas conta no codigo ja estão sendo 'puladas'"

TamCache=0
ConjMap = [0,0]
TamBloco = 4 ###igual a 16 bytes == 2^4
PolitSub= 3
TamMem = 32
mapeamento = ""

def inicio(tCache,Nmap,subst):

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
        Nmap[0] = 0
        Nmap[1] = 1
    elif(escolha2 == 2):
        map = "2-way"
        Nmap[0] = 1
        Nmap[1] =2
    elif(escolha2 == 3):
        map = "4-way"
        Nmap[0] = 2
        Nmap[1] = 4
    elif(escolha2 == 4):
        map = "8-way"
        Nmap[0] = 3
        Nmap[1] = 8
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
    TamConj = tamBloco+tipoMap[0]
    NumConj = numLinhasCache - tipoMap[0]
    index = NumConj
    offSet = tamBloco
    Tag = 32-(index+offSet)
    print(f"\nNumero de linhas :{numLinhasCache}.\nNºConj :{NumConj}\nTam Conj:{TamConj}\n")
    print("=-="*30)
    print("A tag tem {} bits, index tem {} bits, offset tem {} bits.".format(Tag,index,offSet))
    print("=-="*30)
    return(numLinhasCache,index,offSet,Tag)

cache = []
def geraCache(numLinhas,conjMap):
    global cache
    v=[0,0,0,0]
    for i in range(numLinhas*conjMap[1]):
        cache.append(v)

cachehit = 0 
cachemiss = 0
MemReq = 0

completa = False
def Arquivo(index,offset,tag):
    arquivo = open('trace.txt','r')
    for i in arquivo:
        i = int(i, 16)
        i = bin(i)
        i = str(i[2::])
        i = str(i[0:32-offset])
        indexNew = str(i[tag:])
        TagNew = str(i[0:len(i)-index])
        indexNew = int(indexNew, 2)
        TagNew = int(TagNew, 2)
        MemReq +=1
        popular(TagNew,index)
        
def popular(tag,index): 
    global completa
    sai = False
    c = 1
    if completa == False:
        for i in range(len(cache)):
            print(i)
            if(cache[i][0]==0):
                cache[i][0] = 1
                cache[i][1] = tag
                cache[i][2] = 0
                cache[i][3] = 0
                cachemiss += 1
                sai = True
            elif sai == True:
                break
            c+=1
            if c > len(cache):
                completa = True
    

TamCache,ConjMap,PolitSub,mapeamento=inicio(TamCache,ConjMap,PolitSub)
print('Tamanho da Cache : 2^{}, Mapeamento : {} e Politca de Substituição : {}'.format(TamCache,mapeamento,PolitSub))
print("=-="*30)
NumLinhas,index1,offset1,Tag1=calculos(TamBloco,TamCache,ConjMap)
geraCache(NumLinhas,ConjMap)
Arquivo(index1,offset1,Tag1)















