import pandas as pd

df = pd.read_csv('data/GoogleApps.csv')

# print(df.info())
# print(df.head())
# print(df.tail())
# print(round(df['Size'].mean(), 2))
# print(round(df['Size'].median(), 2))
# print(round(df['Price'].max(), 0))
# print(df.describe())


# Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и
# бесплатных приложений ('Type') с точностью до десятых.
# Используй группировку по одному столбцу.
# print(round(df.groupby(by="Type")['Rating'].agg(['min', 'mean', 'max']), 1))


# Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid')
# для разных целевых аудиторий ('Content Rating').
# Используй группировку по одному столбцу.
# df = df[df['Type'] == 'Paid']cl
# print(df.groupby(by="Content Rating")['Price'].agg(['min', 'median', 'max']))


# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом. 
# Посчитай максимальное количество отзывов ('Reviews') в каждой группе.
# Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
# В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?
# Используй сводную таблицу.

# temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
# print(temp[['EDUCATION', 'FAMILY', 'GAME']])

# Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating').
# Посчитай среднее количество отзывов ('Reviews') в каждой группе.
# Выбери названия категорий, в которых есть платные приложения для всех возрастных групп.
# Используй сводную таблицу.

# temp = df[df['Type'] == 'Paid']
# temp = temp.pivot_table(index='Category', columns='Content Rating', values='Reviews', aggfunc='mean')
# print(temp)



# Используй данные, которые тебе удалось получить из набора данных при работе в VSC.
# В каком количестве категорий бесплатных приложений (Type == 'Free') 
# приложения разработаны не для всех возрастных групп ('Content Rating')?

temp = df[df['Type'] == 'Free']
temp = temp.pivot_table(index='Category', columns='Content Rating', values='Reviews', aggfunc='mean')
print(temp)