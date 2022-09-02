from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = (
            'title',
            'text',
            'url',
            'tags',
        )
        widgets = {
            'title': forms.TextInput
        }