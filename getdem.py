import requests
from bs4 import BeautifulSoup
import csv

# что бы подкгрузить зависимости импортов нужно выполнить в терминале в ide
# pip install beautifulsoup4
# pip install lxml

def get_html(url):
    r = requests.get(url)  # Получим метод Response
    r.encoding = 'utf8'
    return r.text  # Вернем данные объекта text


def csv_read(data):
    # with open("data.csv", 'a') as file:
    #   writer = csv.writer(file)
    return data['link']


def get_links(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find_all('div', class_="main-news inf")
    for i in head:
        heads = i.find('div', class_='main-news-image')
        data = {'head': heads.a.img['alt'],
                'link': heads.a.img['src']}
        csv_read(data)

def get_flink(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find_all('div', class_="dmt_list")
    for i in head:
        heads = i.find('div', class_='dmt_list_image_wrapper')
        data = {'head': heads.a.img['alt'],
                'link': heads.a.img['data-src']}
        return csv_read(data)



def get_random():
    data = get_flink(get_html('https://demotivatorium.ru/demotivators/random/'))
    return data