from django import forms
from .models import*
from django.core.exceptions import ValidationError


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title','description','price','auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control from-control-lg'}),
            'description': forms.Textarea(attrs={'class':'form-control form-control-lg', 'cols': 60, 'rows': 18}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'min': 1}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if "?" in title:
            raise ValidationError('Нельзя начинать заголовок с "?"')

        return title
    
