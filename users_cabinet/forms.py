from django import forms

from users.models import Users


class UserPicForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class UserDataForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['login_ke', 'pass_ke']
        widgets = {
            'login_ke': forms.TextInput(attrs={'class': 'form-control mb-3',
                                               'placeholder': 'Введите email или номер телефона'}),
            'pass_ke': forms.PasswordInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Введите пароль'})
        }
