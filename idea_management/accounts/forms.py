from django import forms
from accounts.models import User


class SignInForm(forms.ModelForm):
    remember_me = forms.BooleanField(label='Запомнить меня', required=False)

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта', 'required': True, 'autofocus': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'required': True}),
        }
        labels = {
            'email': '',
            'password': '',
        }
