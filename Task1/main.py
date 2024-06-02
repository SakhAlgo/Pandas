import pandas as pd

df = pd.read_csv('data/GoogleApps.csv')

print(df.info())
# print(df.head())
# print(df.tail())
# print(round(df['Size'].mean(), 2))
# print(round(df['Size'].median(), 2))
# print(round(df['Price'].max(), 0))
# print(df.describe())

# print(round(df['Installs'].mean(), 0))
# print(round(df['Installs'].median(), 0))
# avg_price = dt[dt['Price'].mean()]
# print('Средняя цена приложения:', avg_price)
# print(df[df['Rating'] > 4.9]['Installs'].median())

# Сколько стоит самое дешёвое платное приложение?
# print(df[df['Type'] != 'Free']['Price'].min())

# Чему равна медиана количества установок приложений из категории ART_AND_DESIGN?
# print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())

# На сколько максимальное количество отзывов для бесплатных приложений больше максимального количества отзывов для платных приложений?
# print(len(df[df['Type'] == 'Paid']))
# print(len(df[df['Type'] == 'Free']) - len(df[df['Type'] != 'Free']))

# Каков минимальный размер приложения для тинейджеров?
# print(df[df['Content Rating'] == 'Teen']['Size'].min())


# *К какой категории относится приложение с самым большим количеством отзывов?
# maxValue = df['Reviews'].max()
# print(df[df['Reviews'] == df['Reviews'].max()]['Category'])



# *Каков средний рейтинг приложений стоимостью более 20$ и с количеством установок более 10000?
# С помощью фильтрации по двум условиям выбери из набора данных приложения стоимостью более 20$ и
# с количеством установок более 10000. Определи средний рейтинг таких приложений. 

print(df[(df['Price'] > 20) & (df['Installs'] > 1000)]['Rating'].mean())
