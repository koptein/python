#!/usr/bin/python

from sys import argv

input_string = ''
#input_string = raw_input('Enter Text: ')
script, input_string = argv

output_string = ''

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in input_string:
    myindex  = alphabet.index(letter)
    if myindex >= 13:
        output_string = output_string+alphabet[myindex-13]    
    
    else:
        output_string = output_string+alphabet[myindex+13]

print "Encoded: " , output_string
