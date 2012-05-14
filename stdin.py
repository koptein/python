#!/usr/bin/python

# Example usage:
# python stdin.py < /etc/hosts

# Maybe read stdin linewise, write it to a variable
# and then convert it...
stdin_string = ""

# Read from stdin and just print it.
import fileinput
for line in fileinput.input():
    stdin_string = stdin_string + line

# print whole string.
print stdin_string
