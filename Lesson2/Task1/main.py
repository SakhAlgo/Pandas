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