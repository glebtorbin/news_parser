# Generated by Django 2.2.7 on 2022-09-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.TimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]