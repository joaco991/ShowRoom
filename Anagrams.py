# funcion para identificar anagramas, sin diferenciar entre mayusculas y minusculas, y sin considerar espacios

def aretheyanagrams(str1, str2):

    # condiciona que solo ingresen argumentos en forma de cadenas

    if type(str1) != str or type(str2) != str:
        print("Error, please check the arguments")
        return
    
    # Quitando espacios

    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')

    # llevando ambos textos a mayuscula, no se diferencia entre mayuscula y minuscula en los textos originales

    str1 = str1.upper()
    str2 = str2.upper()

    # se separan y ordenan los puntos en listas para su comparacion

    str1_list = list(str1)
    str2_list = list(str2)

    str1_list.sort()
    str2_list.sort()

    # valor 0 de la variable que determine si son o no anagramas

    var = True

    # primer comparativo, largos de cadenas, si no son iguales de largo, no son anagramas.

    if len(str1_list) != len(str2_list):
        var = False
    
    # si son del mismo largo, se compara elemento a elemento de ambas listas

    else:

        for i in range(len(str1_list)):

            if str1_list[i] == str2_list[i]:
                continue

            else:
                var = False
                break

    # con todos los elementos procesados, se determina si son o no anagramas en funcion de la variable var
    
    if var == True:
        print('They are anagrams')
        return
       
    else:
        print("They are not anagrams")
        return



aretheyanagrams('Listen', 'Silent')
