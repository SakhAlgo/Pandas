import pandas as pd

df = pd.read_csv('data/GoogleApps.csv')
# print(df.info())
# avg_price = dt[dt['Price'].mean()]
# print('Средняя цена приложения:', avg_price)
print(df[df['Rating'] > 4.9]['Installs'].median())