#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./StudentsPerformance.csv')
print(df.info())

# Гипотеза: посещение подготовительных курсов повышает результаты экзаменов
# у абитуриентов из семей, где оба родителя не имеют высшего образования.

# Сортировка по категории 'parental level of education'
# print(df['parental level of education'].value_counts())

# parental level of education
# some college          226
# associate's degree    222
# high school           196
# some high school      179
# bachelor's degree     118
# master's degree        59


df['mean score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3


def set_parents_edication(val):
    if val == "bachelor's degree" or val == "master's degree":
        return 'have ed.'
    return 'no have ed.'
    
df['parents edication'] = df['parental level of education'].apply(set_parents_edication)

# print(df.info())
d = df.pivot_table(index = 'test preparation course', 
 	columns = 'parents edication', 
 	values = 'mean score', 
 	aggfunc = 'mean')

d.plot( kind = 'bar',  grid = True)
plt.show()

