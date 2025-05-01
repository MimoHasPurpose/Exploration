import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.switch_backend('TkAgg')
sns.set_theme()

df=pd.read_csv("student_data.csv")
print(df.head())
df=df[0:3]
print(df.head())

# sns.boxplot(data=df,x="health",y="sex")
# g=sns.PairGrid(df)
# g.map(sns.scatterplot)
plt.show()