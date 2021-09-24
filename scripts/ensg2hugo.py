# !/usr/bin/python3
import sys
import fileinput
import re

ens2gene = {}

with open("gencode.v38.basic.annotation.gtf", 'r') as file:
    for line in file:
        matches = re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";', line)
        if matches:
            # print(matches[0][0])
            # ens2gene[matches[0][0].split('.')[0]] = matches[0][1]
            ens2gene[matches[0][0].split(',')[0]]=matches[0][1]
sample = open('expression_analysis.hugo.csv', 'w')
input_file_to_change = sys.argv[1]
# input_file_to_change = 'expression_analysis.csv'
for each_line_of_expression_analysis in fileinput.input(input_file_to_change):
    splitcolumn_array = re.split(',', each_line_of_expression_analysis.replace('"', '').replace('\n', ''))
    if splitcolumn_array[1] in ens2gene:
        # splitcolumn_array.replace(ens2gene[splitcolumn_array[1]])
        for key, value in ens2gene.items():
            # splitcolumn_array=str(splitcolumn_array)
            splitcolumn_array = str(splitcolumn_array).replace(key, value)
        res = str(splitcolumn_array)[1:-1]
        resmod = res.replace("\'", "")
        print(resmod, file=sample)
sample.close()
