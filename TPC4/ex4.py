import json
import re


def parseFicheiro(file):
    
    f = open(file,"r", encoding='utf-8')
    j = open(file[:-4] + ".json", "w", encoding='utf-8')
    flag = 0

    result = re.findall("(\w+)(\d+|\{\d+\}|\{\d+,\d+\})?(\:\:\w+)?", f.readline())
    print(result)

    regex = "^"
    for resultado in result:
        regex += f"(?P<{resultado[0]}>" + "([\w\s]+"
        flag = 0
        if resultado[1] != "":
            print(resultado[1])
            regex += f"\,?){resultado[1]}(?:,*)?"
            flag = 1
            #for i in range (int(resultado[1][1]) - 1):
                #regex += f",[\w\s]+"

        if flag == 1:
            regex += "),"
        else:
            regex += ")),"

    
    
    regex = regex [:-1]
    regex += "$"
    print(regex)

    linhas = f.readlines()

    for linha in linhas:
        print(linha)
        print("OI")
        resultt = re.match(regex,linha)
        print(resultt)

        dictG = resultt.groupdict()

        for param in dictG:
            listaa = dictG[param].split(",")
            if (len(listaa) > 1):
                listatemp = []
                for elemento in listaa:
                    if elemento != "":
                        listatemp.append(elemento)
                dictG[param] = listatemp
                print("aiaiai")


        json.dump(dictG, j, ensure_ascii=False, indent = 4)



parseFicheiro("alunos.csv")