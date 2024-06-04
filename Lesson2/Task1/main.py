import pandas as pd

df = pd.read_csv('data/GoogleApps.csv')

# print(df.info())
# print(df.head())
# print(df.tail())
# print(round(df['Size'].mean(), 2))
# print(round(df['Size'].median(), 2))
# print(round(df['Price'].max(), 0))
# print(df.describe())


# Сколько всего приложений с категорией ('Category') 'BUSINESS'?
# print(df['Category'].value_counts())

# Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых
# temp = df['Content Rating'].value_counts()
# print(round(temp['Teen'] / temp['Everyone 10+'], 2))

# Найди ответы на вопросы:
# 1. Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? Ответ запиши с точностью до сотых.
# 2. На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.


# temp = df.groupby(by = 'Type')['Rating'].mean()
# print(temp)


# val2 = round(temp['Paid'] - temp['Free'],2)
# print(val2)


# Проанализируй минимальный и максимальный размер приложений
# Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
#  print(df.groupby(by = 'Content Rating')['Size'].agg(['min', ‘max']))

# temp = df[df['Category'] == 'COMICS']
# print(temp['Size'].agg(['min', 'max']))

# print(df.groupby(by = 'Category')['Size'].agg(['min', 'max'])) # второй вариант


# Найди ответы на вопросы:
# 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
# 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?

temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp)
print(temp['FINANCE'])


temp = df[(df['Rating'] > 4.9) & (df['Category'] == 'GAME')]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])
