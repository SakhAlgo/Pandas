import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Выведи информацию о всем DataFrame, чтобы узнать какие столбцы нуждаются в очистке
df.info()
# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
# print(len(df[pd.isnull(df['Rating'])]))

# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
df.fillna({'Rating': -1}, inplace=True)
# df.info()

# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# print(df['Size'].value_counts())

# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.

def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1

df['Size'] = df['Size'].apply(set_size)    
# print(df['Size'].value_counts())

# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
# print(df[df['Category'] == 'TOOLS']['Size'].max())


# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# df['Installs'].apply(int)

# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
def set_installs(inst):
    inst = inst.replace('+', '')
    # print(inst)
    inst = inst.replace(',', '')
    return int(inst)

df['Installs'] = df['Installs'].apply(set_installs)
# df.info()

# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением. 
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?
# temp = df.pivot_table(index='Category', columns='Content Rating', values='Installs', aggfunc='mean')
# temp = temp.apply(round)
# print(temp.max())

# temp = df.pivot_table(index='Content Rating', columns='Type', values='Installs', aggfunc='mean')
# temp = temp.apply(round)
# print(temp)

# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
# temp = df[pd.isnull(df['Type'])]
# print(temp.iloc[0])
df['Type'].fillna('Free', inplace=True)


# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно


# print(df.info())
# Очистка данных из первого задания

# Замени тип данных на дробное число (float) для цен приложений ('Price')
def set_price(price):
    return float(price.replace('$', ''))
        
    
df['Price'] = df['Price'].apply(set_price)

# Вычисли, сколько долларов разработчики заработали на каждом платном приложении

df['Profit'] = df['Price'] * df['Installs']
temp = df[df['Type'] == 'Paid']
# print(temp.info())

# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?
# print(temp['Profit'].max())

# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'
def getAmountGenres(genres):
    if ';' in genres:
        return len(genres.split(';'))
    return 1

df['Number of genres'] = df['Genres'].apply(getAmountGenres)

# print(df.info())
# Какое максимальное количество жанров ('Number of genres') хранится в датасете?
print(df['Number of genres'].max())

# Бонусное задание
# Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last Updated') приложения. Назови его 'Season'
# print(df['Last Updated'].value_counts())
def setSeason(season):
    month = season.split()[0]
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    return '-'
    
df['Season'] = df['Last Updated'].apply(setSeason)   
print(df['Season'].value_counts())
# Выведи на экран сезоны и их количество в датасете
