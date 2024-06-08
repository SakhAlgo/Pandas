#место для твоего кода
import pandas as pd

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

# print(df.describe())
# abit1 = round(df[df['test preparation course'] == 'completed']['writing score'].mean(), 2)
# abit2 = round(df[df['test preparation course'] == 'none']['writing score'].mean(), 2)
# print(abit1, abit2, abit1 - abit2)


groupWithDegree = df[(df['parental level of education'] == "bachelor's degree") | (df['parental level of education'] == "master's degree")]
groupWithoutDegree = df[(df['parental level of education'] != "bachelor's degree") & (df['parental level of education'] != "master's degree")]


print(round(groupWithDegree[groupWithDegree['test preparation course'] == 'completed']['writing score'].mean(), 2))
print(round(groupWithDegree[groupWithDegree['test preparation course'] == 'none']['writing score'].mean(), 2))

print(round(groupWithoutDegree[groupWithoutDegree['test preparation course'] == 'completed']['writing score'].mean(), 2))
print(round(groupWithoutDegree[groupWithoutDegree['test preparation course'] == 'none']['writing score'].mean(), 2))

# группа у кого родители с высшем образованием и прошли курс 79.12
# группа у кого родители с высшем образованием и не прошли курс 71.19
# разница 8%

# группа у кого родители не с высшем образованием и прошли курс  73.36
# группа у кого родители не с высшем образованием и не прошли курс  63.11
# разница ~10%