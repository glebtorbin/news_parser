from django.db import models

class News(models.Model):
    title = models.TextField(verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    url = models.URLField(verbose_name='ссылка')
    tags = models.TextField(verbose_name='теги')
    pub_date = models.TimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.pk}{self.title}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
