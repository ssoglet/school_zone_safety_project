import sys
import csv
import math
import numpy as np
from operator import itemgetter
import time

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="white")

#Load data
data = pd.read_csv('accidents.csv')
df = pd.DataFrame(data)

#Compute the correlation matrix
corr = df.corr()
print(corr)

#Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=np.bool_))

#Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

#Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

#Draw the heatmap with the mask and correct aspect ratio
x = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.8, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

#Show Plot
plt.show()
