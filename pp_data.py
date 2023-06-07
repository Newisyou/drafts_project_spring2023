import pandas as pd
import numpy as np

data_2020_2 = pd.read_excel(
    "2020.09 студ-ком-оцен-тем 2-3 курсы.xlsx", 0)
data_2020_3 = pd.read_excel(
    '2020.09 студ-ком-оцен-тем 2-3 курсы.xlsx', 1)
data_2021_02 = pd.read_excel(
    '2021.02 студ-ком-оцен-тем 2-3 курсы.xlsx')
data_2021_09 = pd.read_excel(
    '2021.09 студ-ком-оцен-тем 2-3 курсы.xlsx', 1)
data_2022_02 = pd.read_excel('2022.02 студ-ком-оцен-тем 2-3 курсы - без оценок (802 чел).xlsx')
data_2022_02_marks = pd.read_excel(
    '2022.02 студ-ком-оцен-тем 2-3 курсы (450 чел).xlsx')
data_2022_09 = pd.read_excel(
    '2022.09 студ-ком-оцен-тем 2-3 курсы.xlsx', 1, header=1)

data_2020_2 = data_2020_2.drop(
    ['Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13',
     'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16'], axis=1)
data_2020_2.replace('', np.nan, inplace=True)
data_2020_2 = data_2020_2.dropna()
data_2020_3 = data_2020_3[['Фамилия', 'Имя', 'Группа', 'Команда', 'Оценка за защиту', 'Название проекта']]
data_2020_3.rename(columns={'Оценка за защиту': 'Защиты'}, inplace=True)
data_2020 = pd.concat([data_2020_2, data_2020_3], ignore_index=True)
data_2020.insert(6, 'Семестр', '2020.09')

data_2021_02 = data_2021_02[['Фамилия', 'Имя', 'Отчество', 'Группа', 'Команда', 'Итоговая оценка', 'Проект']]
data_2021_02.rename(columns={'Итоговая оценка': 'Защиты'}, inplace=True)
data_2021_02.insert(7, 'Семестр', '2021.02')
data_2021_09 = data_2021_09[['Фамилия', 'Имя', 'Отчество', 'Группа', 'Unnamed: 6', 'Оценка', 'Проект']]
data_2021_09.rename(columns={'Оценка': 'Защиты', 'Unnamed: 6': 'Команда'}, inplace=True)
data_2021_09.insert(7, 'Семестр', '2021.09')
data_2021 = pd.concat([data_2021_02, data_2021_09], ignore_index=True)

data_2022_02 = data_2022_02.drop(data_2022_02.columns[0], axis=1)
data_2022_02_marks.rename(
    columns={'Название команды': 'Команда', 'Наименование проекта': 'Проект', 'Экспертная оценка': 'Защиты'},
    inplace=True)
data_2022_02_marks = data_2022_02_marks[['Команда', 'Защиты']]
data_2022_02_marks = data_2022_02_marks.drop_duplicates(ignore_index=True)
df_2022_02 = data_2022_02.merge(data_2022_02_marks, how='left')
df_2022_02.insert(6, 'Семестр', '2022.02')

data_2022_09 = data_2022_09.drop(data_2022_09.columns[0], axis=1)
data_2022_09.insert(5, 'Семестр', '2022.09')
data_2022_09.rename(columns={'Оценка команды студента': 'Защиты'}, inplace=True)

df_2022=pd.concat([df_2022_02,data_2022_09], ignore_index=True)

# data_2020.to_excel('Проектный практикум 2020.xlsx')
# data_2021.to_excel('Проектный практикум 2021.xlsx')
# df_2022.to_excel('Проектный практикум 2022.xlsx')
# df_2022_02.to_excel('Проектный практикум 2022.02.xlsx')
# data_2022_09.to_excel('Проектный практикум 2022.09.xlsx')


data_2020.rename(columns={'Название проекта': 'Проект'}, inplace=True)
data_20_21=pd.concat([data_2020,data_2021], ignore_index=True)
data_20_21=data_20_21[['Фамилия', 'Имя','Отчество','Группа', 'Команда', 'Защиты', 'Проект', 'Семестр']]
# data_20_21.to_excel('Проектный практикум 2020-2021.xlsx')