# Generated by Django 3.2.15 on 2022-09-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.TimeField(auto_now_add=True, verbose_name='дата публикации'),
        ),
    ]