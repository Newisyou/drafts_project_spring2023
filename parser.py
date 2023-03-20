import csv

import requests

# collect_openalex собирает данные в формат json и в дальнейшем преобразует их в список.
# параметры: почта для вежливого пула, фильтер: id project based learning, вывод по 200 записей на каждую страницу,
# переключение страниц через курсор.
# (подробная инфа тут: https://docs.openalex.org/how-to-use-the-api/api-overview)
# Через while переключение страниц. Получает значение нового курсора-перелистывает страницу, считывает,
# нет перехода - данные закончились


def collect_openalex():
    URL_TEMPLATE = 'https://api.openalex.org/works'
    cursor = '*'
    params = {
        'mailto': 'sapfirca@gmail.com',
        'filter': 'concepts.id:C2779825147',
        'per-page': 200,
        'cursor': cursor,
    }
    next_cour = True
    all_works = []
    while next_cour:
        response = requests.get(URL_TEMPLATE, params=params)
        data = response.json()
        work_data = data['results']
        all_works.extend(work_data)
        if data['meta']['next_cursor'] is not None:
            params['cursor'] = data['meta']['next_cursor']
        else:
            next_cour = False
    return all_works


# file_writer(data) преобразовывает полученный список в csv файл. Я записала не все параметры, без понятия,
# понадобятся они или нет. Добавить не трудно. Кодировку стоит прописывать, иначе ругается на непонятные символы


def file_writer(data):
    with open('pr_bas_learn.csv', 'w',encoding="utf-8") as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'title', 'publication_year', 'concepts', 'referenced_works', 'related_works'))
        for works in data:
            concepts=[]
            for i in works['concepts']: 
                concepts.append(i['display_name']) #тут просто решила записать только названия "концепций"
            a_pen.writerow((works['id'], works['title'], works['publication_year'],
                           concepts,
                           works['referenced_works'], works['related_works']))


work_for_write = collect_openalex()
file_writer(work_for_write)
