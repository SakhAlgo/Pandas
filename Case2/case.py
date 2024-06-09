#место для твоего кода
import pandas as pd

df = pd.read_csv('countries of the world.csv')

df.info()

# География, экономика и социология разных стран мира.
# 20 столбцов : численность населения | уровень миграции | показатель ВВП | уровень грамотности |
# количество телефонов | тип экономики | выход к морю и др.

# Идея продукта: социальная реклама.
# Рынок: рекламный рынок.
# Целевая аудитория: государственные учреждения.
# Пример исследовательского вопроса для изучения рынка: какие факторы влияют на качество жизни населения?
# Гипотеза: показатель ВВП зависит от уровня грамотности населения.
# print(df[pd.isnull(df['Literacy (%)'])])
# print(df['Literacy (%)'].value_counts().index[0])
# print(len(df[pd.isnull(df['Rating'])]))
df = df.dropna(subset=['Literacy (%)'])

# print(df.info())
def setLiter(liter):
    return float(liter.replace(',', '.'))

df['Literacy (%)'] = df['Literacy (%)'].apply(setLiter)
# print(df.describe())
# print(df.pivot_table(index='Country', columns='Literacy (%)', values='GDP ($ per capita)'))
print(df.groupby('GDP ($ per capita)')['Literacy (%)'].mean())