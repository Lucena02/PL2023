import re
import collections
import itertools
import json

def anos():
    f = open("processos.txt", "r")
    dicionario = collections.defaultdict(int)

    for linha in f.readlines():
        result = re.search(":(\d{4})-", linha)
        if result == None: pass
        else: dicionario[result.group(1)] += 1
    
    dicionario = collections.OrderedDict(sorted(dicionario.items()))
    for key in dicionario:
        print(str(key) + " -> " + str(dicionario[key]))


def topNomes():
    f = open("processos.txt", "r")
    manyDicts = {}

    for linha in f.readlines():
        data = re.search(":(\d{4})-", linha)
        if data != None: 
            data = int(int(data.group(1))/100 + 1)
            result = re.search("::(\w+)(?:\s*\w+)*\s(\w+)", linha)
            
            if result != None:
                if data not in manyDicts:
                    manyDicts[data] = collections.defaultdict(int)

                manyDicts[data][result.group(1)] += 1
                manyDicts[data][result.group(2)] += 1

    manyDicts = collections.OrderedDict(sorted(manyDicts.items()))
    for key in manyDicts:
        manyDicts[key] = collections.OrderedDict(sorted(manyDicts[key].items(), key=lambda x: x[1]))
        
        print("SÉCULO " + str(key))
        lista = list(manyDicts[key].keys())[-5:]
        lista.reverse()
        for elemento in lista:
            print(elemento + " -> " + str(manyDicts[key][elemento]))
        print("\n")


def relacoes():

    f = open("processos.txt", "r")
    dicts = collections.defaultdict(int)

    for linha in f.readlines():
        result = re.search("[A-Z][a-z]+,((?:[A-Z]\w*\s*){1,})\.", linha)
        

        if result == None: pass
        else:
            relacao = result.group(1)
            dicts[relacao] += 1

    dicts = collections.OrderedDict(sorted(dicts.items(), key=lambda x: x[1]))
    for key in dicts:
        print(key + " -> " + str(dicts[key]))


def jsonex4():
    f = open("answer.json", "w")
    proces = open("processos.txt", "r")

    dictt = {}
    linhas = proces.readlines()
    for i in range(20):
        linha = linhas[i].split("::")
        dictt[i] = {}
        dictt[i]["data"] = linha[0]
        dictt[i]["nome"] = linha[1]
        dictt[i]["pai"] = linha[2]
        dictt[i]["mae"] = linha[3]
        dictt[i]["obs"] = linha[4]
    
    json.dump(dictt, f)

#anos()
#topNomes()
#relacoes()
#jsonex4()