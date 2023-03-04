
def lerTudo():
    acumula =  []
    linha = input("Insira a linha: ")
    curr = ""

    while(linha != "") :
        for char in linha:
            if (curr == ""):
                curr = char 

            else:
                if (char == " "):
                    acumula.append(curr)
                    curr = ""
                elif (curr[0].isdigit()):
                    if (char.isdigit()):
                        curr += char
                    else:
                        acumula.append(curr)
                        curr = char
                elif (curr[0].isalpha()):
                    if (char.isalpha()):
                        curr += char
                    else:
                        acumula.append(curr)
                        curr = char
                else:
                    acumula.append(curr)
                    curr = char
        acumula.append(curr)
        curr = ""
        linha = input("Insira a linha: ")

    acumula.append(curr)
    print(acumula)
    return acumula


def calcula(array):
    r = 0
    flag = True

    for elemento in array:
        if ("on" in elemento.lower()) and ("off" in elemento.lower()):
            if (elemento.lower().index("on") > elemento.lower().index("off")) : flag = True
            else : flag = False
        elif "on" in elemento.lower():
            flag = True
        elif "off" in elemento.lower():
            flag = False
        elif (flag == False):
            pass
        elif (elemento == "="):
            print(r)
        elif (elemento.isdigit()):
            r += int(elemento)
        
calcula(lerTudo())