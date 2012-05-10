#!/usr/bin/python

from sys import argv

input_string = ''

# If there is no argv read the text from console:
if len(argv) == 1 :
    input_string = raw_input('Enter Text: ')
else :
    input_string = argv[1]

output_string = ''

# This looks really dirty, there should be an other way.
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#print type(alphabet)

for letter in input_string:
    #print letter + " -> " + str(type(letter))

    # I can't believe this works...
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
