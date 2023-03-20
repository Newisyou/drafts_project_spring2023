import csv

import requests


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


def file_writer(data):
    with open('pr_bas_learn.csv', 'w',encoding="utf-8") as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'title', 'publication_year', 'authorships', 'concepts', 'referenced_works', 'related_works'))
        for works in data:
            a_pen.writerow((works['id'], works['title'], works['publication_year'], works['authorships'],
                           works['concepts'],
                           works['referenced_works'], works['related_works']))


work_for_write = collect_openalex()
file_writer(work_for_write)
