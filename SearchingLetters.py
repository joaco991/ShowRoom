# Funcion de dos argumentos, se debe definir si las letras del primer argumento estan en el segundo

def searchingletters(search_this, search_here):

    # Condiciona valores de entrada

    if type(search_this) != str or type(search_here) != str:

        print("Error, please verify entry data")
        return
    
    # asegura que no se hayan ingresado espacios en el argumento base de busqueda, y pone todo en mayusculas
    
    search_this = search_this.replace(' ', '')
    search_this = search_this.upper()
    search_here = search_here.upper()

    # genera una lista de las palabras a buscar

    st_list = list(search_this)

    # variable para condicionar resultado

    var = True

    # busqueda de las letras en funcion del metodo find()
    
    for letter in st_list:

        if search_here.find(letter) != -1:

            continue

        else:

            var = False
            break
    
    # cierre de la funcion, segun resultado de variable var
    
    if var == True:

        print("SI")
        return
    
    else:

        print("NO")
        return


searchingletters('gox','sjkiuasfvadjknvbfgrbfro')

