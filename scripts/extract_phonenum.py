#!/usr/bin/python3
import re

with open('/home/bingjing/assignments/trgn_assignment3b/scripts/mytextfile.txt') as phone:
        a = phone.read()

p1 = re.compile("([0-9]{2,4}[-.\s]{,1}){3,4}", re.MULTILINE)
b=p1.search(a).group(0)
b1=b.replace('-', ' (',1)
b2=b1.replace('-', ') ',1)
b3=b2.replace('-','')
b4='+'+b3
print(b4)
p2 = re.compile("([0-9]{3,4}[-.\s]{1}){3}", re.MULTILINE)
c=p2.search(a).group(0)
c1='('+c
c2=c1.replace('-', ')',1)
c3=c2.replace('.','')
c4=c3.replace('-','')

print(c4)
