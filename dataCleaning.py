import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset
df = pd.read_csv('student-mat(in).csv')
print(df)
print(df.isnull())	#check for missing values on 2nd dataset

#scatter plots comparing G1, G2 and G3
G1G2Plot = sns.scatterplot(data=df, x='G1', y='G2')
G1G2Plot.set_xlabel('G1')
G1G2Plot.set_ylabel('G2')
#plt.show()

G1G3Plot = sns.scatterplot(data=df, x='G1', y='G3')
G1G3Plot.set_xlabel('G1')
G1G3Plot.set_ylabel('G3')
#plt.show()

G2G3Plot = sns.scatterplot(data=df, x='G2', y='G3')
G2G3Plot.set_xlabel('G2')
G2G3Plot.set_ylabel('G3')
#plt.show()

#boxplots for address scores(G1, G2, G3)
addressScores1 = sns.boxplot(data=df, x='address', y='G1').set(title='Semester 1')	#G1 plot
plt.show()

addressScores2 = sns.boxplot(data=df, x='address', y='G2').set(title='Semester 2')	#G2 plot
plt.show()

addressScores3 = sns.boxplot(data=df, x='address', y='G3').set(title='Final Grade')	#G1 plot
plt.show()