#!/usr/bin/python
from string import split
import whois
import sys
import string
"""
script to try and see what domains are available
"""

# file with list of sylables seprated by spaces
infile = open("sylables.txt");
text = infile.read()
infile.close()
syb = split(text) # this is now an array of sylables

# output file
outfile= open('possible-domains.txt', 'r+')


domains = [(x + y + '.com') for x in syb for y in syb if x != y]

for maybe in domains:
    res = whois.query(maybe)
    if(res is not None):
        print "too bad " + res.name + " is taken"
    else:
        print "behold..." + maybe
        outfile.write(maybe + '\n')
        outfile.flush()

outfile.close()
