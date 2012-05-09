#!/usr/bin/python

from sys import argv

input_string = ''

# If there is no argv read the text from console:
if len(argv) == 1 :
    input_string = raw_input('Enter Text: ')
else :
    input_string = argv[1]

output_string = ''

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in input_string:
# Exclude Numbers:
    if not letter.isdigit():
        myindex  = alphabet.index(letter.lower())
        if myindex >= 13:
            output_string = output_string+alphabet[myindex-13]    
        
        else:
            output_string = output_string+alphabet[myindex+13]

print  output_string
