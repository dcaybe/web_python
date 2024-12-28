from django import forms
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

    


#class Insert_computer_form(forms.ModelForm):
#     class Meta:
#         model = Computer
#         fields = '__all__'



# class Computer_search_computer(forms.Form):
#    computer_name = forms.CharField()
#    computer_type = forms.ModelChoiceField(
#        queryset = Computer_type.objects.all(),
#        required=False,
#        label=" Chọn loại máy tính"
#     )

# class Insert_user_form(forms.ModelForm):
#     class Meta:
#         model = account
#         fields = '__all__'


# class Thiet_lap_cuoc_choi_form(forms.ModelForm):
#     class Meta:
#         model = Computer_account
#         fields = '__all__'
#         exclude = ['start_time','end_time']

# class Thiet_lap_cuoc_choi_form(forms.ModelForm):
#     class Meta:
#         model=Computer_account
#         fields = '__all__'
#         exclude = ['start_time', 'end_time']
#     def __init__(self, *args, **kwargs): 
#         super().__init__(*args, **kwargs)
# # Chỉ hiển thị các tài khoản không có phiên đang chơi 
#         self.fields['account'].queryset =account.objects.exclude( 
#         computer_account__end_time__isnull=True
#         )
# # Chỉ hiển thị các máy không ở trạng thái 'Đang chơi' 
#         self.fields['computer'].queryset =Computer.objects.exclude( 
#             trang_thai='Đang chơi'
#         )
# dùng user có sẵn của django
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','password'] # chỉ lấy ra username và password