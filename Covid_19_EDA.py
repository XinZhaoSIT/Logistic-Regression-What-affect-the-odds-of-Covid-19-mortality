import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('COVID-19_Case_Data_Clean.csv')

age = df.loc[df['death_yn']=='Yes'].groupby('age_group').death_yn.value_counts()
sns.set_style("whitegrid")
sns.set_color_codes("pastel")
sns.set(font_scale = 2)
plt.figure(figsize=(10,6))
sns.barplot(age.index,age.values)
plt.xlabel('Age Group')
plt.ylabel('Number of deaths')
plt.title('Number of deaths group by age')
plt.xticks(rotation=45)
plt.show()

