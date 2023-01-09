# Juego TIC TAC TOE donde comienza la maquina con X, en el centro, y luego de cada interaccion coloca aleatorio en los lugares disponibles

# tablero sin interacciones

board = [[1, 2, 3], [4, 5, 6], [7, 8,9]]

# funcion de muestra de tablero

def DisplayBoard(board):

    borde = "+-------+-------+-------+"
    lat = "|"

    print(borde)

    for elem in board:
        
        print(lat,lat,lat,lat,sep="       ")

        for i in elem:
            print(lat, "   ", i, "   ", sep = "", end = "")

        print(lat)
        print(lat,lat,lat,lat,sep="       ")
        print(borde)


# reemplaza en la lista board, el numero a elegir por el simbolo 'O' y muestra el nuevo estado del trablero

def EnterMove(board):

    move = int(input("Ingresa tu movimiento: "))
    
    if move<1 or move>9:
        
        print("celda inexistente")
        return
    
    elif move>0 and move<10:
        
        for i in range(len(board)):
            
            for j in range(len(board[i])):
                
                if board[i][j]==move:
                    
                    board[i][j] = "O"
                    DisplayBoard(board)
                    return board
                
                elif i==2 and j==2:
                    
                    print("Lugar ya ocupado")
                    DisplayBoard(board)
                    return board


# genera una lista de tuplas, donde cada tupla son las "coordenadas" de un espacio disponible de juego

def MakeListOfFreeFields(board):
    
    FreeFields = []

    for i in range(len(board)):
        
        for j in range(len(board[i])):
            
            if board[i][j]=="O" or board[i][j]=="X":

                continue

            else:

                FreeFields.append((i,j))
                
    return FreeFields


# define situaciones de victoria, ganador o empate, ademas continua el juego en funcion de la situacion del juego y de quien haya jugado ultimo

def VictoryFor(board, sign):

    count_a= 0
    count_b= 0
    
    for i in range(len(board)):
        
        if board[i][i]== sign:

            count_a +=1
            
            if count_a==len(board):

                print("Ganador:", sign)
                return True
            
        if board[i][-(i+1)]== sign:

            count_b +=1
            
            if count_b==len(board):

                print("Ganador:", sign)
                return True
            
        if board[i][0]== sign:
            
            if board[i][0]==board[i][1] and board[i][1]==board[i][2]:

                print("Ganador:", sign)
                return True
                
        if board[0][i]== sign:
            
            if board[0][i]==board[1][i] and board[1][i]==board[2][i]:

                print("Ganador:", sign)
                return True
                
        if i==len(board)-1 and MakeListOfFreeFields(board)!= []:

            if sign == "X":

                EnterMove(board)

            elif sign == "O":

                DrawMove(board)

        elif i == len(board)-1 and MakeListOfFreeFields(board) == []:

            print("Ha sido un empate!")
            return True


# el primer movimiento y la eleccion aleatoria del equipo en sus turnos posteriores

def DrawMove(board):

    FreeFields=MakeListOfFreeFields(board)
    
    from random import randrange
    PCmove=randrange(10)
    
    if board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:

        board[1][1] = "X"
        DisplayBoard(board)
        return board
    
    else:

        for elem in FreeFields:

            if board[elem[0]][elem[1]] == PCmove:

                for i in range(len(board)):

                    for j in range(len(board[i])):
                        
                        if board[i][j]== PCmove:
                
                            board[i][j] = "X"
                            DisplayBoard(board)
                            return board
                
            elif elem==FreeFields[len(FreeFields)-1]:

                DrawMove(board)

# Funcion iniciadora de juego

def Game(board):

    signs = ["O", "X"]

    for sign in signs:

        if VictoryFor(board,sign)== True:

            return

        elif sign == "O":

            continue

        elif sign == "X":
            
            Game(board)


DisplayBoard(board)
Game(board)
