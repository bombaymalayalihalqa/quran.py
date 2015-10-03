#!/usr/bin/python
target=open('abc.txt','w')
target.write('Swabira\n')
target.write('Ameeen\n')
for x in range(10):
    target.write("%d\n" %x)


