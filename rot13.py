#!/usr/bin/python

from sys import argv

#Initializing variables
input_string = ''
output_string = ''
alphabet = []
alphabet_upper = []

# Ask for text if more or less than one argument.
if len(argv) != 2:
    input_string = raw_input('Enter Text: ')
else :
    input_string = argv[1]

for char in map(chr, xrange(97, 123)):
    alphabet.append(char)

for char in map(chr, xrange(65, 90)):
    alphabet_upper.append(char)

for letter in input_string:
    #print letter + " -> " + str(type(letter))

    use = alphabet_upper
    if letter.islower():
        use = alphabet

    # Exclude Numbers:
    if letter.isdigit():
        output_string = output_string+letter

    else:
        myindex  = alphabet.index(letter.lower())
        if myindex >= 13:
                output_string = output_string+use[myindex-13]
        
        else:
            output_string = output_string+use[myindex+13]

print  output_string
