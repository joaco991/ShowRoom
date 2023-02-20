# Given a text file, return the amount of times each letter appears in it

# starting with introducing the text file
source = input("Please introduce the text file: ")

# Opening the file
from os import strerror

try:

    s_op = open(source, 'rt')

except IOError as e:

    print('An error has ocurred while opening the file', strerror(e.errno))


# Working through the file

dict = {}
numbers = [str(i) for i in range(10)]
upper_letters = [i+65 for i in range(26)]
lower_letters = [i+97 for i in range(26)]


try:
    
    s_reading = s_op.read(1)

except IOError as e:

    print('An error has ocurred while reading the file', strerror(e.errno))
    s_op.close()

try:

    while s_reading > 0:

        # if not a letter, continue
        if ord(s_reading) == 32 or s_reading in numbers:

            s_reading = s_op.read(1)
            continue
    
        # if an upper letter, make it a lower one and add it to the dictionary
        elif ord(s_reading) in upper_letters:

            s_reading = s_reading.lower()
        
            if s_reading in dict.keys():

                dict[s_reading] += 1

            else:

                dict[s_reading] = 1

            s_reading = s_op.read(1)
            continue
    
        # if a lower letter, just goes into the dictionary
        elif ord(s_reading) in lower_letters:

            if s_reading in dict.keys():

                dict[s_reading] += 1
        
            else:

                dict[s_reading] = 1

            s_reading = s_op.read(1)
            continue
        
        else:
            
            s_reading = s_op.read(1)
            continue
    
    s_op.close()

except IOError as e:

    print('An error has ocurred when trying to read the file', strerror(e.errno))
    s_op.close()

# prepearing the presentation

if dict != {}:
    
    sorted(dict)

    # Showing the values
    for key in dict:

        print(key, '->', dict[key], end = '\n')

else:
    print('Text has not been detected on file')
