#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path= "/home/bingjing/assignments/trgn_assignment3b/scripts/expression_analysis.csv"
df=pd.read_csv(path)
fig = plt.figure(figsize=(12,4))    

plt.grid(axis='y', alpha=0.75)
plt.xticks(fontsize=10)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('510 Age Histogram')
plt.savefig("./Age_histogram.png")
