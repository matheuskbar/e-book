from django import forms
from django.db.models import fields

from createbook.models import Ebook
from .models import Ebook


class FormEbook(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = '__all__'