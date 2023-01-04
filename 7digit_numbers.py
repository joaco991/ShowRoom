# Ingresando un numero entero, la funcion debe devolver su version de 7 digitos, sin importar el numero ingresado

#  funcion preparatoria, prepara el formato de los numeros a llamar, cada numero es una lista, donde cada elemento de la lista es una fila del numero.

def digitnumberblock(string, column):

    # se definieron las 4 estructuras primarias de construccion de numeros

    full = '# # #  '
    right = '    #  '
    left = '#      '
    sides = '#   #  '

    # se definieron las estructuras de los numeros en listas, para luego ser llamadas por fila.

    one = [right for i in range(5)]
    two = [full, right, full, left, full]
    three = [full, right, full, right, full]
    four = [sides, sides, full, right, right]
    five = [full, left, full, right, full]
    six = [full, left, full, sides, full]
    seven = [full, right, right, right, right]
    eight = [full, sides, full, sides, full]
    nine = [full, sides, full, right, full]
    zero = [full, sides, sides, sides, full]

    # condiciona el tipo de valores que necesita la funcion

    if type(column) != int:

        print("Error", column, "must be a number")
        return

    if type(string) != str:
        
        print("Error", string, "must be a number as text")
        return

    # esta funcion devuelve el bloque de construccion para cada fila segun su numero

    if string == '1':

        return one[column]
    
    elif string == '2':

        return two[column]
    
    elif string == '3':
        
        return three[column]
    
    elif string == '4':
        
        return four[column]

    elif string == '5':
        
        return five[column]

    elif string == '6':
        
        return six[column]

    elif string == '7':

        return seven[column]

    elif string == '8':
        
        return eight[column]

    elif string == '9':

        return nine[column]

    elif string == '0':

        return zero[column]
    
    else:

        return "Error, please check the text"


# Funcion principal, transforma el numero original y busca en la funcion anterior las lineas necesarias para la conversion

def digitnumber(number):

    # condicionando el valor ingresado
    if type(number) != int:

        print("Error", number, "must be a number")
        return
    
    # Convierto el numero int en str primero y luego en una lista

    numberstr = str(number)
    listnum = list(numberstr)

    # para cada elemento de la lista, se le asigna el bloque de la fila correspondiente

    for i in range(5):
        line = ''
        aux = None
        for item in listnum:
            aux = digitnumberblock(item, i)
            line = line + aux
        
        # imprimo cada linea por separado, siendo numeros generados en 5 lineas, verificando la misma lista una y otra vez.

        print(line)



    return



digitnumber(0)