from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from accounts.models import MyUser


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )

    password2 =forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password and password2 and password2 != password:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password2')