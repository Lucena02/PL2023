import json


def parseFicheiro(file):
    
    f = open(file,"r", encoding='utf-8')
    j = open(file[:-4] + ".json", "w", encoding='utf-8')
    dict = {}
    titulos = f.readline().split(",")
    for i in range(len(titulos)):
        titulos[i] = titulos[i].strip()
        dict[titulos[i]][j] = []

    check = 0
    for linha in f.readlines():
        print(linha)
        nomes = linha.split(",")
        for i in range (len(titulos)):
            dict[titulos[i]][check] = nomes[i]
        check += 1

        

    json.dump(dict, j, ensure_ascii=False, indent = 4)


parseFicheiro("alunos.csv")