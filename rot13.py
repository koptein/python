#!/usr/bin/python

from sys import argv
import fileinput

#Initializing variables
input_string = ''
output_string = ''
alphabet = []
alphabet_upper = []
use_argv = False

#functions

def readfile( filename ):
    text = ""
    myfile = open(filename)
    for line in myfile:
        if line != "":
            text =  text + line
    print "DEBUG:filecontent_= "+text
    return text
    
# Ask for text if more or less than one argument.
if len(argv) < 2:
    input_string = raw_input('Enter Text: ')
else:
# check for filehandling

    for element in argv:
        if element == "-f":
            print "DEBUG: File argument detected"
            filename = argv[argv.index(element)+1]
            print "DEBUG:filename= "+filename 
            input_string = readfile(filename)

if use_argv: 
    input_string = argv[1]
#Filling the Alphabet arrays from the ascii table

for char in map(chr, xrange(97, 123)):
    alphabet.append(char)

for char in map(chr, xrange(65, 90)):
    alphabet_upper.append(char)

#Actually swap the letters

for letter in input_string:
    #print letter + " -> " + str(type(letter))

    use = alphabet_upper
    if letter.islower():
        use = alphabet

    # Exclude non alpha characters from conversion.
    if not letter.isalpha():
        output_string = output_string+letter

    else:
        myindex  = alphabet.index(letter.lower())
        if myindex >= 13:
            output_string = output_string+use[myindex-13]
        else:
            output_string = output_string+use[myindex+13]

print  output_string
