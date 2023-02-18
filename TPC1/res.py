
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

        
def sexoDoença():
    indice = 0
    m = 0
    f = 0
    for inteiro in doença:
        if (inteiro == "1"):
            if (sexo[indice] == "M"): m += 1
            else: f += 1
        indice += 1
    print("Doentes do sexo Masculino: " + str(m) + "\n" + "Doentes do sexo Feminino: " + str(f))
        

def divide(a,b):
    if (b == 0):
        return 0
    else: return a/b

def ageRange():
    list = dict.fromkeys(range(18), 0)
    total = dict.fromkeys(range(18), 0)
    indice = 0
    for age in idade:
        if (age == "idade") : pass
        else :
            if (doença[indice] == "1") :
                list[int((int(age))/5)] += 1
            total[int((int(age))/5)] += 1
        indice += 1
    
    print("Doentes de acordo com a sua faixa etária:\n")
    for i in range(18):
        print(str(i*5) + "-" + str((i+1)*5-1) + ": " + str(list[i]) + " de " + str(total[i]) + " doentes -> " + str(divide(list[i],total[i])*100) + "%")


def colesterolRange():
    list = dict.fromkeys(range(61), 0)
    total = dict.fromkeys(range(61), 0)
    indice = 0
    for colesterol in col:
        print(colesterol)
        if (colesterol == "colesterol") : pass
        else :
            if (doença[indice] == "1") :
                list[int((int(colesterol))/10)] += 1
            total[int((int(colesterol))/10)] += 1
        indice += 1
    
    print("Doentes de acordo com o seu colesterol:\n")
    for i in range(61):
        print(str(i*10) + "-" + str(i*10+10) + ": " + str(list[i]) + " de " + str(total[i]) + " doentes -> " + str(divide(list[i],total[i])*100) + "%")

def main():
    parsing("myheart.csv")
    #sexoDoença()
    #ageRange()
    colesterolRange()

main()
