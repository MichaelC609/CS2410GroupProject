import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset
df = pd.read_csv('student-mat(in).csv')
print(df)
print(df.isnull().sum())	#check for missing values on 2nd dataset

#scatter plots comparing G1, G2 and G3
G1G2Plot = sns.scatterplot(data=df, x='G1', y='G2')
G1G2Plot.set_xlabel('Grade 1')
G1G2Plot.set_ylabel('Grade 2')
plt.show()

G1G3Plot = sns.scatterplot(data=df, x='G1', y='G3')
G1G3Plot.set_xlabel('Grade 1')
G1G3Plot.set_ylabel('Grade 3')
plt.show()

G2G3Plot = sns.scatterplot(data=df, x='G2', y='G3')
G2G3Plot.set_xlabel('Grade 2')
G2G3Plot.set_ylabel('Grade 3')
plt.show()

MeduPlot = sns.boxplot(data = df, x = 'G3', y = 'Medu', orient = 'h')
MeduPlot.set_xlabel('Grade 3')
MeduPlot.set_ylabel('Mother\'s Education')
plt.show()

FeduPlot = sns.boxplot(data = df, x = 'G3', y = 'Fedu', orient = 'h')
FeduPlot.set_xlabel('Grade 3')
FeduPlot.set_ylabel('Father\'s Education')
plt.show()
