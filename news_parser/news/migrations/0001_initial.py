# Generated by Django 2.2.7 on 2022-09-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='текст')),
                ('url', models.URLField(verbose_name='ссылка')),
                ('tags', models.TextField(verbose_name='теги')),
            ],
        ),
    ]
