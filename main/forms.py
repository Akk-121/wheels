from .models import  CustomUser, regist, questions, select, shop
from django import forms
from django.forms import ModelForm, TextInput, FileInput, EmailInput, PasswordInput, Textarea, RadioSelect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class shopForm(ModelForm):
    class Meta:
        model = shop
        fields = ['name', 'text', 'price', 'img']
        widgets = {
            'name' : TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'img': FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
            }),
        }


class registform(ModelForm):
    class Meta:
        model = regist
        fields = ['username', 'name', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш никнейм'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ваш email'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите пароль',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль',
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['username'] == '' or ' ' in cd['username']:
            raise forms.ValidationError('Вы должны указать свой username')

        elif CustomUser.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('Пользователь с таким username существует!')

        elif CustomUser.objects.filter(email=cd['email']).exists() and CustomUser.objects.filter(email=cd['email']).first().is_active:
            raise forms.ValidationError('Пользователь с таким email существует!')

        elif cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')

        elif len(cd['password1']) < 6 or len(cd['password2']) < 6:
            raise forms.ValidationError('Пароль должен быть больше 6 сиволов')

        return cd['password2']

class questionsForm(ModelForm):
    class Meta:
        model = questions
        fields = ['about', 'first_name', 'last_name', 'number', 'email']
        widgets = {
            'about': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите свой вопрос',
                'id' : "text",
                'style' : "max-height: 150px"
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'id': "firstName"
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'id': "lastName"
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email@mail.ru',
                'id': "email"
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
                'id': "number"
            }),
        }


class templateselect(forms.Form):
    sh = shop.objects.filter(radio='Шины')

    # diametr 1
    diametr_list = []
    for i in range(len(sh)):
        if sh[i].diametr not in diametr_list:
            diametr_list.append(sh[i].diametr)
    diametr_list.sort()

    CHOICES1 = [
        ['Диаметр (R)', 'Диаметр (R)'],
    ]
    for i in diametr_list:
        x = [i, i]
        CHOICES1.append(x)

    diametr = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-select',
        'id': "validationServer01",
    }), choices=CHOICES1)


    #shirina 2
    shirina_list = []
    for i in range(len(sh)):
        if sh[i].shirina not in shirina_list:
            shirina_list.append(sh[i].shirina)
    shirina_list.sort()

    CHOICES2 = [
        ['Ширина профиля', 'Ширина профиля'],
    ]
    for i in shirina_list:
        x = [i, i]
        CHOICES2.append(x)

    shirina = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-select',
        'id': "validationServer02",
    }), choices=CHOICES2)


    #  profil 3
    profil_list = []
    for i in range(len(sh)):
        if sh[i].profil not in profil_list:
            profil_list.append(sh[i].profil)
    profil_list.sort()

    CHOICES3 = [
        ['Высота профиля', 'Высота профиля'],
    ]
    for i in profil_list:
        x = [i, i]
        CHOICES3.append(x)

    profil = forms.ChoiceField(widget=forms.Select(attrs={
                'class': 'form-select',
                'id': "validationServer03",
            }), choices=CHOICES3)


    # season 4
    CHOICES4 = [
        ('Сезон', 'Сезон'),
        ('Лето', 'Лето'),
        ('Зима Шип', 'Зима Шип'),
        ('Зима Не Шип', 'Зима Не Шип')
    ]

    season = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-select',
        'id': "validationServer03",
    }), choices=CHOICES4)

    # manufacturer 5
    manufacturer_list = []
    for i in range(len(sh)):
        if sh[i].manufacturer not in manufacturer_list:
            manufacturer_list.append(sh[i].manufacturer)
    manufacturer_list.sort()

    CHOICES5 = [
        ['Производитель', 'Производитель'],
    ]

    for i in manufacturer_list:
        x = [i, i]
        CHOICES5.append(x)

    manufacturer = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-select',
        'id': "validationServer03",
    }), choices=CHOICES5)

    def clean_password2(self):
        cd = self.cleaned_data
        return cd['diametr']