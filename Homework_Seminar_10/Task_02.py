# Задача 2. Постройте диаграмму с данными о численности студентов дневной формы обучения 
# южного федерального округа за 2017 год.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/78d/78d77b235f7b3b14e1ac671e61435311.csv',
                sep=';', encoding='cp1251')
df = df.iloc[33:41, :]
df = df[['Субъект РФ', 'Численность студентов, очная форма, человек, 2017']]

plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(labels = df['Субъект РФ'], rotation = 90)

plt.show()
