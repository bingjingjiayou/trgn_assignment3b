import matplotlib.pyplot as plt

with open('/home/bingjing/assignments/trgn_assignment3b/scripts/expression_analysis.tsv')

#  matplotlib.axes.Axes.hist()
n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()

plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
