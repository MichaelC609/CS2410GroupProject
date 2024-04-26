import pandas as pd 

#load the dataset
df = pd.read_csv('student-por.csv')
print(df.isnull())	#dataset contains no missing values


