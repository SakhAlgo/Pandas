#место для твоего кода
# Характеристика нескольких сот блюд по множеству параметров.
# 24 столбца: калорийность блюд | соотношение БЖУ | содержание полезных микроэлементов и др.

# Идея продукта: приложение для генерации меню, соответствующего критериям ЗОЖ.
# Рынок: рынок общественного питания.
# Целевая аудитория: представители ЗОЖ.
# Пример исследовательского вопроса для изучения рынка: каким набором продуктов в McDonald's
# можно заменить один приём пищи, не превышая норму калорий?
# Гипотеза: на завтрак в McDonald's можно подобрать комбинацию продуктов, соответствующую нормам здорового питания.

#  1:1:4, в которой на одну часть белков и одну часть жиров приходится 4 части углеводов.

import pandas as pd

df = pd.read_csv('menu.csv')

# print(df.describe())
# print(df.info())
print(df[['Item', 'Protein', 'Total Fat', 'Carbohydrates']])

df = df[['Item', 'Protein', 'Total Fat', 'Carbohydrates', 'Calories']]
print(df[(df['Calories'] < 600) & (df['Carbohydrates'] / df['Protein'] > 3) & (df['Carbohydrates'] / df['Protein'] < 5) & (df['Carbohydrates'] / df['Total Fat'] > 3) & (df['Carbohydrates'] / df['Total Fat'] < 5)])