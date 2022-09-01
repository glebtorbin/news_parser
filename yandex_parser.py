import requests
from bs4 import BeautifulSoup
import fake_useragent


url = 'https://market.yandex.ru/partners/news'

user= fake_useragent.UserAgent().random
header = {'user-agent': user}

response = requests.get(url, headers=header).text
soup = BeautifulSoup(response, 'html.parser')
blocks = soup.find("section", class_='main-layout')
links = blocks.find_all('a', class_='link link_theme_normal news-list__item-active i-bem')[:10]
url_list = []
for link in links:
    result_link = link.get('href')
    result_yandex_link = f'https://market.yandex.ru/{result_link}'
    url_list.append(result_yandex_link)
title_list = []
info_list = []
tags_list = []
for content in url_list:
    response = requests.get(content, headers=header).text
    soup = BeautifulSoup(response, 'html.parser')
    titles = soup.find("div", class_="news-info__title").text
    title_list.append(titles)
    info = soup.find("div", class_="news-info__post-body html-content page-content").text
    info_list.append(info)
    tags = soup.find("div", class_="news-info__tags").text
    tags_list.append(tags)
