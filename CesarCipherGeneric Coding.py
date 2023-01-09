# Codigo para codificar hacia abajo, la B la vuelvo A.


def cesarecipher(string, moves):

    #  Condicionando los valores ingresados

    if type(string) != str:
        return "Error, must insert text"
    
    if type(moves) != int:
        return "Error, must insert a number between 1 and 25"
    
    if moves < 1 or moves > 25:
        return "Error, must insert number between 1 and 25"
    
    cipher = ''

    # string = string.replace(' ', '')

    # Valor diferencia para los puntos que se vayan del abecedario en la resta.

    moveup = 26 - moves

    for ch in string:

        # Para los simbolos, numeros y espacios mantengo sus valores.

        if not ch.isalpha():
            cipher += ch
        
        # Para las mayusculas, sus valores ASCII van desde el 65, en caso de que bajen, se le debe sumar 26

        elif ord(ch) == ord(ch.upper()):

            if (ord(ch) - moves) < 65:
                code = ord(ch) + moveup
                cipher += chr(code)

            else:
                code = ord(ch) - moves
                cipher += chr(code)
        
        # Para minusculas, si baja del valor ASCII 97, se le debe sumar 26. 

        elif ord(ch) != ord(ch.upper()):

            if (ord(ch) - moves) < 97:
                code = ord(ch) + moveup
                cipher += chr(code)
            
            else:
                code = ord(ch) - moves
                cipher += chr(code)
    
    print(cipher)
    return