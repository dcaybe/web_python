from django import forms
from .models import *

class Insert_vi_tri_form(forms.ModelForm):
    class Meta:
        model = Vi_tri
        fields = '__all__'

class Insert_Mode_form(forms.ModelForm):
    class Meta:
        model = Mode
        fields = '__all__'

class Insert_nhan_vien_form(forms.ModelForm):
    class Meta:
        model = nhan_vien
        fields = '__all__'

class nv_search(forms.Form):
   vi_tri = forms.ModelChoiceField(
       queryset = Vi_tri.objects.all(),
       required=False,
       label=" Chọn chức vụ"
    )