from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class ThemesForm(forms.ModelForm):
    class Meta:
        model = Themes
        fields = '__all__'


class RegForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'nickname': 'Прозвище',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['commentcontent', 'commentimg']
