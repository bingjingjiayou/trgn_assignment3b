#!/usr/bin/python3
import re
ens2gene={}

with open("gencode.v38.basic.annotation.gtf", 'r') as file:
    for line in file:
         matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
         if matches:
             print(matches[0][0])
             ens2gene[matches[0][0]]=matches[0][1]
             
