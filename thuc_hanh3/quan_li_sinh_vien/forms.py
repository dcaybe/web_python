from django import forms
from .models import *

class Insert_Major_form(forms.ModelForm):
    class Meta:
        model = sinh_vien
        fields = '__all__'

class Insert_Departments_form(forms.ModelForm):
    class Meta:
        model = Majors
        fields = '__all__'