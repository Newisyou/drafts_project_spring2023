import pandas as pd

# подгружаем csv
df = pd.read_csv('pr_bas_learn.csv', delimiter=',')
tab_names = ['id', 'title', 'concepts', 'abstract_inverted_index', 'authorships', 'best_oa_location', 'biblio',
             'cited_by_api_url',
             'cited_by_count', 'counts_by_year', 'doi', 'is_retracted', 'locations',
             'primary_location', 'publication_date', 'type',
             'updated_date',
             'publication_year', 'referenced_works', 'related_works']

# Создаем csv файл, который преобразуем в граф. Обработка столбца с работами, на которые ссылается текущая
csv_graph = df[['id', 'referenced_works']]
csv_graph['referenced_works'] = csv_graph['referenced_works'].str.replace('[', '')
csv_graph['referenced_works'] = csv_graph['referenced_works'].str.replace(']', '')
csv_graph['referenced_works'] = csv_graph['referenced_works'].str.replace("'", '')
csv_graph['referenced_works'] = csv_graph['referenced_works'].str.replace(" ", '')

# gephi понимает граф в виде связного списка в формате csv. Разделяем referenced_works на отдельные столбцы.
# Меняем None на пустую строку. В csv сохраняем без индекса и заголовка
new = csv_graph['referenced_works'].str.split(',', expand=True)
new = new.fillna('')
final_pd = pd.concat([csv_graph['id'], new], axis=1)
# final_pd.to_csv('cites.csv', index=False, header=None)
