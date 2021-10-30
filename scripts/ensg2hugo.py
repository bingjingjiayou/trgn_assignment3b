# !/usr/bin/python3
import sys
import fileinput
import re

ens2gene = {}

args3b=sys.argv[1:]

if len(args3b)<1:
    print('arguments are needed')
    exit
if '-f' in args3b[0]:
    flag=int(args3b[0][-1])
    input_file_to_change=args3b[1]
else:
    flag=1
    input_file_to_change=args3b[0]

with open("Homo_sapiens.GRCh37.75.gtf",'r') as file:
    for line in file:
        matches=re.findall('gene_id "(.*?)".*gene_name "(.*?)";',line)
        if matches:
             ens2gene[matches[0][0].split(',')[0]]=matches[0][1]

for line in fileinput.input(input_file_to_change):
    geneid_key=re.findall('(E[^\.]+)',line)[0]
    arrays=re.split(',',line)
    if geneid_key in ens2gene:
        newline=re.sub(str(arrays[flag-1]),str(ens2gene[geneid_key]),line)
        print(str(newline))
