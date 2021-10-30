#!/usr/bin/python3
import re
mtf=open('mytextfile.txt')
try:
    all_text = mtf.read()
finally:
    mtf.close()
#print(all_text)
for line0 in re.findall(r"[+]{0,1}[0-9]{2,3}[-][0-9]{2,4}[-][0-9]*[-]{0,1}[0-9]*", all_text):
        
        wholephone= re.split("-", line0)
       
        phone2 = "("+wholephone[-3]+")"+wholephone[-2]+wholephone[-1]
        #print(phone2)
        if wholephone[0][0] == "+":
            phone2 = wholephone[0]+phone2
        print(phone2)
