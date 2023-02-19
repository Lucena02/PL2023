
idade = []
sexo = []
tensao = []
col = []
batimento = []
doença = []

def parsing(ficheiro) :
    f = open(ficheiro, "r")
    for line in f :
        linhaSep = line.split(",")
        idade.append(linhaSep[0])
        sexo.append(linhaSep[1])
        tensao.append(linhaSep[2])
        col.append(linhaSep[3])
        batimento.append(linhaSep[4])
        doença.append((linhaSep[5])[:-1])


        # AUXILIARES -----------------------------------------

def divide(a,b):
    if (b == 0):
        return 0
    else: return a/b

def maxi(lista):
    maximo = 0
    for x in lista:
        try:
            if int(x) > maximo:
                maximo = int(x)
        except ValueError:
            pass
    return maximo


        # QUERY 1 ---------------------------------------------

def sexoDoença():
    indice = 0
    m = 0
    f = 0
    for inteiro in doença:
        if (inteiro == "1"):
            if (sexo[indice] == "M"): m += 1
            else: f += 1
        indice += 1

    return (m,f)
    


def drawSexoDoença(t):
    print(" Doentes de acordo com o seu sexo")
    print(" Masculino   Feminino")
    print(" " + str(t[0]) + " " * (12-(len(str(t[0])))) + str(t[1]) + " " * (10-(len(str(t[1])))))




        # QUERY 2 ---------------------------------------------

def ageRange():
    maximo = int(maxi(idade))
    maximo = int(maximo/5 + 1)
    list = dict.fromkeys(range(maximo), 0)
    total = dict.fromkeys(range(maximo), 0)
    indice = 0
    for age in idade:
        if (age == "idade") : pass
        else :
            if (doença[indice] == "1") :
                list[int((int(age))/5)] += 1
            total[int((int(age))/5)] += 1
        indice += 1

    return (list, total, maximo)
    
    

def drawAgeRange(list):
    print("\nDoentes de acordo com a sua faixa etária:\n \n")

    print(" Faixa etária    Nº Doentes    Nº Saudaveis    Percentagem ")
    for i in range(list[2]):
        print(" " + str(i*5) + "-" + str((i+1)*5-1) + " " * (15 - (len(str(i*5)) + len(str((i+1)*5-1))))  + str(list[0][i]) + " " * (14 - len(str(list[0][i])))  + str(list[1][i]) + " " * (16 - len(str(list[1][i]))) + str(round(divide(list[0][i],list[1][i])*100, 2)) + "%")


        # QUERY 3 ---------------------------------------------

def colesterolRange():
    maximo = int(maxi(col))
    maximo = int(maximo/10 + 1)
    list = dict.fromkeys(range(maximo), 0)
    total = dict.fromkeys(range(maximo), 0)
    indice = 0
    for colesterol in col:
        if (colesterol == "colesterol") : pass
        else :
            if (doença[indice] == "1") :
                list[int((int(colesterol))/10)] += 1
            total[int((int(colesterol))/10)] += 1
        indice += 1

    return(list,total,maximo)
    
    


def drawColesterolRange(list):
    print("\nDoentes de acordo com o seu nível de colesterol:\n \n")

    print(" Colesterol    Nº Doentes    Nº Saudaveis    Percentagem ")
    #for i in range(maximo):
        #print(str(i*10) + "-" + str(i*10+10) + ": " + str(list[i]) + " de " + str(total[i]) + " doentes -> " + str(divide(list[i],total[i])*100) + "%")
    for i in range(list[2]):
        print(" " + str(i*10) + "-" + str(i*10+10) + " " * (13 - (len(str(i*10)) + len(str(i*10+10))))  + str(list[0][i]) + " " * (14 - len(str(list[0][i])))  + str(list[1][i]) + " " * (16 - len(str(list[1][i]))) + str(round(divide(list[0][i],list[1][i])*100, 2)) + "%")

        # MAIN

def main():
    parsing("myheart.csv")
    opcao = 0
    while opcao != 4 :
        print("[1] Doentes por sexo \n[2] Doentes por idades\n[3] Doentes por colesterol\n[4] Sair")
        opcao = int(input("Selecione uma opcao:"))
        if opcao == 1:
            drawSexoDoença(sexoDoença())
        elif opcao == 2:
            drawAgeRange(ageRange())
        elif opcao == 3:
            drawColesterolRange(colesterolRange())
        elif opcao == 4:
            print("A encerrar...")
            break
        else:
            print("Comando nao reconhecido")


main()
