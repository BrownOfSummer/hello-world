#!/usr/bin/python
# -*- coding: utf-8 -*-
a = 100
if a >= 0:
    print a
else:
    print -a

#integer
# 1 -8 0xff0

#float
#1.23 -3.14 0.000012==1.2e-5

#string
#'abc' "I'm OK"->6 char
# Escape character \
#'I\'m \"OK\"!' == I'm "OK" !
print 'I\'m ok.'
print '\\\n\\'
# \n \t \\
print '\\\t\\'
print r'\\\t\\'
print '''line1
line2
line3'''
# True Fasle
print 3 > 2
# and or not
print True or True
print False and False
print False or False
# empty -> None
print '10/3 =',10/3
print '10.0/3=',10.0/3
# coding
print ord('A')
print chr(65)
print 'len(\'ABC\') =',len('ABC')
print 'len(\'AB C\') =',len('AB C')

# format output
# %d integer %f->float %s->string %x->0x
print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%d' % ('Jack',1000)

print '%2d-%02d' % (3, 1)
print '%.3f' % 3.14159



















