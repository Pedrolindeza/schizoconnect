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

df1 = pd.read_table("schizoconnect/" + "BrainGluSchi" +".txt", sep = ',', header = 0, low_memory = False)
df2 = pd.read_table("schizoconnect/" + "Cobre" +".txt", sep = ',', header = 0, low_memory = False)
df3 = pd.read_table("schizoconnect/" + "FBirn" +".txt", sep = ',', header = 0, low_memory = False)
df4 = pd.read_table("schizoconnect/" + "MCIC" +".txt", sep = ',', header = 0, low_memory = False)
df5 = pd.read_table("schizoconnect/" + "NU" +".txt", sep = ',', header = 0, low_memory = False)
df6 = pd.read_table("schizoconnect/" + "Nusdast" +".txt", sep = ',', header = 0, low_memory = False)

meta = pd.read_table("schizoconnect/" + "MetaData" +".txt", sep = ',', header = 0, low_memory = False)
MetaData = meta.drop(['study','projectid','description','age','sex'], axis = 1)

dfs = [df1,df2,df3,df4,df5,df6]

for df in dfs:
	for index, row in df.iterrows():
		if (row['question_value']=='9999' or row['question_value']=='8888' or row['question_value']=='88888'):
			df.drop([index], inplace=True)

for x in range(0,6):	
	dfs[x] = dfs[x].drop(['source','study','site','visit','assessment','assessment_description'], axis=1)

data = pd.concat(dfs)

index = data.subjectid.unique()
columns = data.question_id.unique()

print("columns = ", len(columns))
print ("rows = ", len(index))

main = pd.DataFrame(index=index, columns=columns)

for index, row in data.iterrows():
	main.at[row["subjectid"], row["question_id"]] = row["question_value"]

main.index.name = 'subjectid'
main = pd.merge(main, MetaData, on="subjectid", how="right")

main.to_csv('joined_data.csv',sep=',')

print("\nSAVED")