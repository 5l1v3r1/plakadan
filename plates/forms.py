from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from plates.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='İsim',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim*'}))
    last_name = forms.CharField(max_length=30, label='Soyisim',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim*'}))
    email = forms.EmailField(max_length=254, label='E-posta',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-posta*'}))
    username = forms.CharField(label='Kullanıcı Adı',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı*'}))
    phone_number = forms.CharField(label='Telefon Numarası', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Telefon Numarası*'}))
    password1 = forms.CharField(label='Parola',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola*'}))
    password2 = forms.CharField(label='Parola(Tekrar)',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Parola(Tekrar)*'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2',)


class UpdateProfileForm(ModelForm):
    first_name = forms.CharField(max_length=30, label='İsim',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim*'}))
    last_name = forms.CharField(max_length=30, label='Soyisim',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim*'}))
    email = forms.EmailField(max_length=254, label='E-posta',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-posta*'}))
    phone_number = forms.CharField(label='Telefon Numarası', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Telefon Numarası*'}))

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable']:
                self.fields[i].widget.attrs['class'] = 'form-control'

        if hasattr(self, 'readonly'):
            for x in self.readonly:
                self.fields[x].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number',)
