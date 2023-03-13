import json
import re


def parseFicheiro(file):
    
    f = open(file,"r", encoding='utf-8')
    j = open(file[:-4] + ".json", "w", encoding='utf-8')

    result = re.findall("(\w+)(\d+|\{\d+\}|\{\d+,\d+\})?(\:\:\w+)?", f.readline())
    print(result)

    regex = ""
    for resultado in result:
        regex += f"(?P<{resultado[0]}>[\w\s]+"
        if resultado[1] != "":
            print(resultado[1])
            for i in range (int(resultado[1][1]) - 1):
                regex += f",[\w\s]+"

        regex += "),"

    
    
    regex = regex [:-1]
    print(regex)

    linhas = f.readlines()

    for linha in linhas:
        print("OI")
        resultt = re.match(regex,linha)

        dictG = resultt.groupdict()

        for param in dictG:
            listaa = dictG[param].split(",")
            if (len(listaa) > 1):
                listatemp = []
                for elemento in listaa:
                    listatemp.append(elemento)
                dictG[param] = listatemp
                print("aiaiai")


        json.dump(dictG, j, ensure_ascii=False, indent = 4)



        

    #json.dump(dict, j, ensure_ascii=False, indent = 4)


parseFicheiro("alunos.csv")