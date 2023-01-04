# Funcion que encuentra frases o palabras capicuas

def palindrome(string):

    # condiciona tipo de argumento para seguir con la funcion

    if type(string) != str:
        print("Error, insertar texto")
        return
    

    # brinda un formato analizable a la cadena, quita espacios, convierte todo a mayuscula y lo vuelve una lista: un elemento es un caracter

    string = string.replace(' ', '')
    string = string.upper()
    strlist = list(string)

    # variables de funcionamiento para la comparacion
    
    var = len(strlist) // 2
    aux = True

    # la comparacion modifica la variable aux en caso de no ser capicua
    for i in range(var):

        if strlist[i] == strlist[-i-1]:
            continue

        else:
            aux = False
            break
    
    # salidas de texto ante resolucion

    if aux == True:
        print("La palabra es capicua")
        return
    
    else:
        print("La palabra no es capicua")
        return



palindrome('Ten animals I slam in a net')
palindrome('i am not a polindrome')
    

    