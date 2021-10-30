#!/usr/bin/python3
import pandas as pd
import sys
import matplotlib.pyplot as plt

args3b = sys.argv[1:]

print(args3b)

if args3b[0].startswith('-f'):
    axis = int(args3b[0][-1])
    file3b = sys.argv[2]
    df = pd.read_csv(file3b)
   
else:
    axis = 1
    file3b = sys.argv[1]
    df = pd.read_csv(file3b)

df.iloc[:,axis].hist()
plt.savefig("./laboratory_data.png")
