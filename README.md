Для запуска проекта:
- установить зависимости
- сделать миграции
- запустить команду python manage.py parse_start

## Описание проекта:
Приложение собирает посление новости с Яндекса и созраняет их в админку, реализованную на Django Admin LTE3

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/glebtorbin/quiz-app.git
```
```
cd news_parser
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
Запусить сбор новостей
```
python3 manage.py parse_start
```
