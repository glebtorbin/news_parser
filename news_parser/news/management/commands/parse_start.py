import requests
from bs4 import BeautifulSoup
import fake_useragent
from django.core.management.base import BaseCommand
from news.models import News


url = 'https://market.yandex.ru/partners/news'
def parse():
    user= fake_useragent.UserAgent().random
    header = {'user-agent': user}
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, 'html.parser')
    blocks = soup.find("section", class_='main-layout')
    links = blocks.find_all('a', class_='link link_theme_normal news-list__item-active i-bem')[:10]
    url_list = []
    title_list = []
    info_list = []
    tags_list = []
    for link in links:
        result_link = link.get('href')
        result_yandex_link = f'https://market.yandex.ru/{result_link}'
        url_list.append(result_yandex_link)
    for content in url_list:
        response = requests.get(content, headers=header).text
        soup = BeautifulSoup(response, 'html.parser')
        titles = soup.find("div", class_="news-info__title").text
        title_list.append(titles)
        info = soup.find("div", class_="news-info__post-body html-content page-content").text
        info_list.append(info)
        tags = soup.find("div", class_="news-info__tags").text
        tags_list.append(tags)
    for i in range(10):
        News(title=title_list[i],
             text=info_list[i],
             url=url_list[i],
             tags=f'#Yandex{tags_list[i]}').save()
    for url1 in News.objects.values_list('url', flat=True).distinct(): 
        News.objects.filter(pk__in=News.objects.filter(url=url1).values_list('pk', flat=True)[1:]).delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        parse()

