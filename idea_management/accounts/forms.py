from django import forms
from accounts.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
                'required': True,
                'autofocus': True,
                'id': 'inputEmail',
                'type': 'email'
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'required': True,
                'id': 'inputPassword',
                'type': 'password'
            }
        )
    )
    remember_me = forms.BooleanField(label='Запомнить меня', required=False)

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name', 
            'email', 
            'password', 
            'is_administrator', 
            'is_manager',
            'is_author'
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Никнейм',
                    'required': True, 
                    'autofocus': True,
                    'type': 'user',
                    'id': 'name'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя',
                    'required': True, 
                    'autofocus': True,
                    'type': 'user',
                    'id': 'first_name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фамилия',
                    'required': True, 
                    'autofocus': True,
                    'type': 'user',
                    'id': 'last_name'
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Почта', 
                    'required': True, 
                    'autofocus': True,
                    'id': 'inputEmail',
                    'type': 'email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Пароль', 
                    'required': True,
                    'id': 'inputPassword',
                    'type': 'password'
                }),
            'is_administrator': forms.CheckboxInput(
                attrs={
                    'type': 'checkbox',
                    'value': 'admin'
                }),
            'is_manager': forms.CheckboxInput(
                attrs={
                    'type': 'checkbox',
                    'value': 'manager'
                }),
            'is_author': forms.CheckboxInput(
                attrs={
                    'type': 'checkbox',
                    'value': 'author'
                }),

        }
        labels = {
           'username': '',
           'first_name': '',
           'last_name': '',
           'email': '',
           'password': ''
        }
