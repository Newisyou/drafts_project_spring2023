
import pandas as pd

articles = pd.read_excel('stati_bez_goda.xlsx')
l1 = pd.read_csv('out.csv')
l2 = pd.read_csv('out1.csv')
l3 = pd.read_csv('out2.csv')
l4 = pd.read_csv('out3.csv')
l5 = pd.read_csv('out4.csv')
l6 = pd.read_csv('out5.csv')

l1 = l1["''"].tolist()
l2 = l2["''"].tolist()
l3 = l3["''"].tolist()
l4 = l4["''"].tolist()
l5 = l5["''"].tolist()
l6 = l6["''"].tolist()

res = l1 + l2 + l3 + l4 + l5 + l6
articles['year'] = res
len(res)
len(articles)
articles.to_csv('Articles.csv')