import ply.lex as lex
import re 

tokens = (
    "LEVANTAR",
    "POUSAR",
    "MOEDA",
    "CONTACTO",
    "ABORTAR"
)

t_LEVANTAR = r"LEVANTAR"
t_POUSAR = r"POUSAR"
t_ABORTAR = r"ABORTAR"

saldo = 0
flag = 0 # 0 = telefone pousado, 1 = telefone levantado, 2 = abortar


def t_MOEDA(t):
    r"MOEDA\s((\w+\,?\s?)+)"
    match = re.match(r"MOEDA\s((\w+\,?\s?)+)", t.value)
    t.value = match.group(1)
    return t

def t_CONTACTO(t):
    r"T\=(\d{9})"
    match = re.match(r"T\=(\d{9})", t.value)
    t.value = match.group(1)
    return t

def t_error(t):
    print("Erro")
    t.lexer.skip(1)

def t_whitespace(t):
    r"\s+"
    pass


def calculaSaldo(): # Transforma saldo atua em formato XeYc
    global saldo
    euros = int(saldo/100)
    centimos = round(saldo/100 - int(saldo/100), 2)
    string = str(euros) + "e" + str(int(centimos*100)) + "c"
    return string


def parseMoedas(listaMoedas): # Verificar input de moedas recebidas
    global saldo
    print(listaMoedas)
    #moedinhas = listaMoedas.split(",")
    #print(moedinhas)
    resultc = re.findall("\d+(?=c)", listaMoedas)
    resulte = re.findall("\d+(?=e)", listaMoedas)
    string = "maq: "

    for numero in resultc:
        if (int(numero) != 1 and int(numero) != 2 and int(numero) != 5 and int(numero) != 10 and int(numero) != 20 and int(numero) != 50):
            string += str(numero) + "c -> moeda inválida;"
        else: 
            saldo += int(numero)

    for numero in resulte:
        if (int(numero) != 1 and int(numero) != 2):
            string += str(numero) + "e -> moeda inválida;"
        else: 
            saldo += int(numero)*100

    string += "saldo = " + calculaSaldo()
    print(string)        



def parseContacto(contacto):
    global saldo

    if (contacto[:3] == "601" or contacto[:3] == "641"):
        print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
    
    elif (contacto[:2] == "00"):
        if (saldo > 150):
            saldo -= 150
            print("maq: saldo = " + calculaSaldo())
        else:
            print("maq: Saldo Insuficiente")

    elif (contacto[:1] == "2"):
        if (saldo > 25):
            saldo -= 25
            print("maq: saldo = " + calculaSaldo())
        else:
            print("maq: Saldo Insuficiente")

    elif (contacto[:3] == "800"):
        print("maq: saldo = " + calculaSaldo())

    elif (contacto[:3]):
        if (saldo > 10):
            saldo -= 10
            print("maq: saldo = " + calculaSaldo())
        else:
            print("maq: Saldo Insuficiente")
    else: print("maq: Contacto inválido")

def parse(token):
    global flag 

    if (token.type == "LEVANTAR"):
        if (flag == 0): 
            print("maq: Introduza moedas.")
            flag = 1
        else: print("maq: O telefone já se encontra levantado...")
    
    elif (token.type == "POUSAR"):
        if (flag == 1): 
            saldoFinal = calculaSaldo()
            print("maq: Troco =" + saldoFinal + "; Volte sempre!")
            flag = 0
        else: print("maq: O telefone já se encontra pousado...")

    elif (token.type == "MOEDA"):
        if(flag == 0):
            print("maq: O telefone está pousado...")
        else: parseMoedas(token.value)

    elif (token.type == "CONTACTO"):
        if (flag == 0):
            print("maq: O telefone está pousado...")
        else: parseContacto(token.value)
    
    elif (token.type == "ABORTAR"):
        flag = 2
    else:
        print("Erro no input")



def lexerr():
    lexer = lex.lex()
    while(True):
        info = input("> ")
        lexer.input(info)
        for token in lexer:
            parse(token)
        if (flag == 2): break

lexerr()