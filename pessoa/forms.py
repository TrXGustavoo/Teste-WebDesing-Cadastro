from tabnanny import check
from django import forms
from django.forms import  models, fields
from .models import Profile 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nome_completo', 'idade', 'intolerancia_a_Gluten', 'intolerancia_a_Lactose']
