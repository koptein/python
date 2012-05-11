#!/usr/bin/python

# Example usage:
# python stdin.py < /etc/hosts

# Read from stdin and just print it.
import fileinput
for line in fileinput.input():
    print line
