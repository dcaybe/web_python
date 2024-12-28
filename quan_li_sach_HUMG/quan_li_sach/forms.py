from django import forms
from .models import *

class Insert_loai_sach_form(forms.ModelForm):
    class Meta:
        model = Loai_sach
        fields = '__all__'

class Insert_nhom_hoc_phan_form(forms.ModelForm):
    class Meta:
        model = Nhom_hoc_phan
        fields = '__all__'

class Insert_sach_form(forms.ModelForm):
    class Meta:
        model =   sach  
        fields = '__all__'

class Insert_user_form(forms.ModelForm):
    class Meta:
        model = account
        fields = '__all__'

class Thiet_lap_muon_sach_form(forms.ModelForm):
    class Meta:
        model=Sach_account
        fields = '__all__'
        exclude = ['start_time', 'end_time']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
# Chỉ hiển thị các tài khoản không có phiên đang chơi 
        # self.fields['account'].queryset =account.objects.exclude( 
        # computer_account__end_time__isnull=True
        # )
# Chỉ hiển thị các máy không ở trạng thái 'Đang chơi' 
        self.fields['sach'].queryset =sach.objects.exclude( 
            so_luong=0
        )
