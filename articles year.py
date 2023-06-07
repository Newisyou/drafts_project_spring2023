import csv
import asyncio
from aiohttp import ClientSession
import pandas as pd


async def get_sites(sites):
    tasks = [asyncio.create_task(fetch_site(s)) for s in sites]
    return await asyncio.gather(*tasks)


async def fetch_site(url):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 404:
                dat = ''
            else:
                dat = await resp.json()
    return dat


df = pd.read_excel('stati_bez_goda.xlsx')  # список статей
iter_df = df['Label']
URL_TEMPLATE = 'https://api.openalex.org/works'
all_years = []
file = open("out5.csv", "w")

def years():
    for i in range(24000,len(iter_df)):
        param = str(iter_df[i])
        sites = [f"{URL_TEMPLATE}/{param}?select=publication_year"]  # перебираем id статьи
        data = asyncio.run(get_sites(sites))
        if data[0]=='':
            year=data
        else:
            year=data[0]['publication_year']
        year=str(year)
        file.write(year+'\n')
        all_years.append(year)

years()
file.close()
# df['Year'] = all_years
