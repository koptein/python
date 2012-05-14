#!/usr/bin/python

from sys import argv
import fileinput
from Rot13 import Rot13

#Initializing variables
input_string = ''
output_string = ''
debug = False
use_argv = True

# TODO:
# - If arguments contains "-" read input from stdin
#   See stdin.py, there is a working example.
# - Use argparse to handle all cli arguments,
#   which should make above task easier as well.

# Check if Verbose Mode is on:
for element in argv:
    if element == "-v":
        debug = True
#functions

def readfile( filename ):
    text = ""
    myfile = open(filename)
    for line in myfile:
        if not line.strip():
            continue
        else:
            text =  text + line
    if debug:        
        print "DEBUG:filecontent_= "+text
    return text
    
# Ask for text if more or less than one argument.
if len(argv) < 2:
    input_string = raw_input('Enter Text: ')
else:
# check for filehandling

    for element in argv:
        if element == "-f":
            use_argv = False
            if debug:
                print "DEBUG: File argument detected"
            filename = argv[argv.index(element)+1]
            if debug:
                print "DEBUG:filename= "+filename 
            input_string = readfile(filename)

if use_argv: 
    input_string = argv[1]

Rotator = Rot13(input_string)
output_string = Rotator.rotate()

print  output_string
