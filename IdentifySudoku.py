# Programa que identifique si los 9 numeros de 9 digitos ingresados pueden armar un sudoku

def IdentifySudoku(num1, num2, num3, num4, num5, num6, num7, num8, num9):

    sudoku = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
    

    # verifico que sean numeros y que tengan 9 digitos

    for number in sudoku:

        if type(number) != int:

            print('Error,', number, 'is not correct')
            return
        
        if number < 123456789 or number > 987654321:

            print('Error,', number, 'is not correct')
            return
        

    base = [str(i+1) for i in range(9)]
    numlist = ['' for i in range(9)]
    sudoku_str = ['' for i in range(9)]
    sudoku_list = ['' for i in range(9)]

    for i in range(9):
        
        # asi genero una lista, donde cada elemento debe ser una lista ordenada de los valores cada argumento
        # agarro un argumento, lo vuelvo str, luego lo convierto a lista y luego lo ordeno.

        # 1. vuelvo cada argument int un string, desde la lista sudoku
        sudoku_str[i] = str(sudoku[i])
        # 2. armo una lista nueva, donde cada elemento sea una lista formada por el str correspondiente de sudoku_str
        sudoku_list[i] = list(sudoku_str[i])
        # 3. genero una lista ordenada para poder compararlos luego
        numlist[i] = sorted(sudoku_list[i])


        # comparo linea a linea para verificar que cada argumento tiene los 9 numeros del 1 al 9, sino, no es un sudoku
        if base != numlist[i]:

            print('Not a sudoku')
            return
        
    
    # recorro verticalmente el sudoku, entro en una columna, y voy fila por fila primero, quitando los numeros de base_aux hasta cubrir las 9 filas y los 9 numeros.
    # luego paso a la siguiente columna y repito

    for i in range(9):

        base_aux = base[:]

        for j in range(9):

            try:
                
                place = base_aux.index(sudoku_list[j][i])
                del(base_aux[place])
            
            except:
                
                print("Not a sudoku")
                return


    # si no genero ningun error, es un sudoku
       
    print("A complete sudoku")
    return


IdentifySudoku(295743861, 431865927, 876192543, 387459216, 612387495, 549216738, 763524189, 928671354, 154938672)
    
    