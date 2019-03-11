import math

"Algumas conta no codigo ja estão sendo 'puladas'"

tamCache=0
TipoMap = ''
TamBloco = 4

def inicio(tCache,map,bloco):

    print("=-="*30)
    print("Escolha o Tamanho da cache :\n1º 1MB\n2º 2MB\n3º 4MB\n4º 8MB\n5º 16MB \n")
    escolha1=6
    while(escolha1 > 5 or escolha1 < 1):
        escolha1=int(input("Escolha : "))
    if (escolha1 == 1):
        tCache=20
    elif(escolha1==2):
        tCache=21
    elif(escolha1==3):
        tCache=22
    elif(escolha1==4):
        tCache=23
    elif(escolha1==5):
        tCache=24 
    print("=-="*30)
    print("Escolha o tipo de mapeamento :\n1º Direto\n2º 2-way\n3º 4-way\n4º 8-way\n")
    escolha2=5
    while(escolha2 > 4 or escolha2 < 1):
        escolha2=int(input("Escolha : "))
    if (escolha2 == 1):
        map = "Direto"
    elif(escolha2 == 2):
        map = "2-way"
    elif(escolha2 == 3):
        map = "4-way"
    elif(escolha2 == 4):
        map = "8-way"
    print("=-="*30)
    
    return(tCache,map)

tamCache,TipoMap=inicio(tamCache,TipoMap,Tan)



