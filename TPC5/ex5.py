import re

def numeroCheck(numero, saldo):
    


def func():
    saldo = 0

    while(True):
        linha = input()
        coisa = re.match(r"\w+", linha)
        print(coisa.group())

        if(coisa.group() == "ABORTAR"):
            print("maq: Troco devolvido: " + str(saldo))
            break
        elif (re.match("T\=[0-9]{9}",linha)):
            linha = linha[2:10]
            print(linha)



func()