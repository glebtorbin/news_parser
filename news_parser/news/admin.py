from django.contrib import admin
from .models import News
from .forms import NewsForm

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'url', 'tags', 'pub_date')
    form = NewsForm


