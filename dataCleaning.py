import pandas as pd 

#load the dataset
df = pd.read_csv('student-por.csv')
print(df.isnull())	#dataset contains no missing values

df2 = pd.read_csv('student-mat.csv')
print(df.isnull())	#check for missing values on 2nd dataset