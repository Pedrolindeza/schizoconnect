# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import numpy as np

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

df = pd.read_csv("joined_data.csv", sep=',', header = 0, low_memory = False)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

#limpar menos de 30 obs
for column in df:
	if (column == 'subjectid' or column == 'dx') : continue
	if (int(df.at[1293,column]) < 30):
		df = df.drop([column],axis=1)


df_mean = df.groupby('dx').mean()
df_std = df.groupby('dx').std()

df_g = pd.concat([df_mean, df_std])

df_g.to_csv('distributions.csv',sep=',')

print("SAVED")