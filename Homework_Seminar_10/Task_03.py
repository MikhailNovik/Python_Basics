# Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, 
# в которых общее количество студентов не превышает 10000 за данный год.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/78d/78d77b235f7b3b14e1ac671e61435311.csv',
                sep=';', encoding='cp1251')

df = df[['Субъект РФ', 'Численность студентов, всего человек, 2019', 'Численность студентов заочная форма, человек, 2019']]

msk = df['Субъект РФ'].str.contains('федерация|федеральный', case=False, na=False)
df = df.drop(df[msk].index)

df = df[df['Численность студентов, всего человек, 2019'] <= 10000]

plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов заочная форма, человек, 2019')
plot.set_xticklabels(labels = df['Субъект РФ'], rotation = 90)

plt.show()
