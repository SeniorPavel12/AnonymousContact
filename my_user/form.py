from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth import get_user_model


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        if email:
            try:
                user = get_user_model().objects.get(email=email)
                check_pass = user.check_password(password)
                if check_pass is False:
                    raise Exception('Password/Email error')
            except Exception as e:
                raise ValidationError(e)
            return password
        else:
            raise ValidationError('Введите все поля')


class PostProfileForm(forms.ModelForm):
    class Meta:
        model = ProfilePostModel
        fields = ['title', 'content']


