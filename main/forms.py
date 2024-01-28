from .models import  CustomUser, regist, questions, select, shop, files
from django import forms
from django.forms import ModelForm, TextInput, FileInput, EmailInput, PasswordInput, Textarea, Select
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class fileForm(ModelForm):
    class Meta:
        model = files
        fields = ['name', 'file']
        widgets = {
            'name': TextInput(attrs={
                'id': 'name_file',
                'class': 'form-control mb-2',
                'placeholder': 'Название файла'
            }),
            'file': FileInput(attrs={
                'class': 'form-control mb-2',
                'type': 'file',
                'accept': '.xlsx'
            })
        }

class shopForm(ModelForm):
    class Meta:
        model = shop
        fields = ['diametr', 'shirina', 'profil', 'manufacturer', 'model_manufacturer', 'season', 'radio', 'type', 'name', 'text',
                  'price', 'ostatok', 'speed', 'ves', 'img']
        CHOICES4 = [
            ('Сезон', 'Сезон'),
            ('Лето', 'Лето'),
            ('Зима Шип', 'Зима Шип'),
            ('Зима Не Шип', 'Зима Не Шип')
        ]
        CHOICES3 = [
            ('Категория', 'Категория'),
            ('Шины', 'Шины'),
            ('Диски', 'Диски')
        ]

        CHOICES2 = [
            ('Тип', 'Тип'),
            ('Литой', 'Литой'),
            ('Штампованный', 'Штампованный'),
            ('Кованый', 'Кованый')
        ]

        widgets = {
            'diametr': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Диаметр (Шины/Диски)'
            }),
            'shirina': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина (Шины) / Вылет (Диски)'
            }),
            'profil': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Профиль (Шины)/ Крепеж (Диски)'
            }),
            'manufacturer': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Производитель (Шины/Диски)',
                'id': 'shirina'
            }),
            'model_manufacturer': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Модель (Шины/Диски)'
            }),
            # ======================================

            'season' : Select(attrs={
                'class': 'form-select mb-2',
                'id': "season",
            }, choices=CHOICES4),

            'radio': Select(attrs={
                'class': 'form-select mb-2',
                'id': "radio",
            }, choices=CHOICES3),

            'type': Select(attrs={
                'class': 'form-select mb-2',
                'id': "type",
            }, choices=CHOICES2),

            # ========================================
            'name' : TextInput(attrs={
                'class':'form-control mb-2',
                'placeholder': 'Название'
            }),
            'text': Textarea(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Описание'
            }),
            'price': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Цена'
            }),
            'img': FileInput(attrs={
                'class': 'form-control mb-2',
                'type': 'file',
                'accept': 'image/png, image/jpeg'
            }),
            # ==========================================='ostatok', 'speed', 'ves'
            'ostatok': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Остаток на складе'
            }),
            'speed': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Индекс скорости (Шины)'
            }),
            'ves': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Индекс нагрузки (Шины)'
            }),
        }


class registform(ModelForm):
    class Meta:
        model = regist
        fields = ['name', 'email', 'number', 'password1', 'password2']
        widgets = {
            # 'username': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введите ваш логин'
            # }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'aria-describedby': "emailHelp",
                'placeholder': 'Укажите ваш email'
            }),
            'number': TextInput(attrs={
                'class': 'form-control tel',
                'id': 'tel',
                'type': 'tel',
                'name': 'tel',
                'placeholder': 'Введите ваш номер телефона'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Укажите пароль',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Повторите пароль',
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        # if cd['username'] == '' or ' ' in cd['username']:
        #     raise forms.ValidationError('Вы должны указать свой username')

        # elif CustomUser.objects.filter(username=cd['username']).exists():
        #     raise forms.ValidationError('Пользователь с таким username существует!')

        if CustomUser.objects.filter(email=cd['email']).exists() and CustomUser.objects.filter(email=cd['email']).first().is_active:
            raise forms.ValidationError('Пользователь с таким email существует!')

        elif CustomUser.objects.filter(number=cd['number']).exists() and CustomUser.objects.filter(number=cd['number']).first().is_active:
            raise forms.ValidationError('Пользователь с таким номером существует!')

        elif cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')

        elif len(cd['password1']) < 8 or len(cd['password2']) < 8:
            raise forms.ValidationError('Пароль должен быть больше 8 сиволов')

        return cd['password2']

class questionsForm(ModelForm):
    class Meta:
        model = questions
        fields = ['about', 'first_name', 'last_name', 'number', 'email', 'who']
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
            'who': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'who',
                'id': "who",
                'type': 'hidden'
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
        'id': "diametr",
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
        'id': "shirina",
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
                'id': "profil",
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
        'id': "season",
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
        'id': "manufacturer",
    }), choices=CHOICES5)

    def clean_password2(self):
        cd = self.cleaned_data
        return cd['diametr']


class templateselect_discks(forms.Form):
    sh = shop.objects.filter(radio='Диски')

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
        ['Вылет (ЕТ)', 'Вылет (ЕТ)'],
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
        ['Крепеж', 'Крепеж'],
    ]
    for i in profil_list:
        x = [i, i]
        CHOICES3.append(x)

    profil = forms.ChoiceField(widget=forms.Select(attrs={
                'class': 'form-select',
                'id': "validationServer03",
            }), choices=CHOICES3)


    # type 4
    CHOICES4 = [
        ('Тип', 'Тип'),
        ('Литой', 'Литой'),
        ('Штампованный', 'Штампованный'),
        ('Кованый', 'Кованый')
    ]

    type = forms.ChoiceField(widget=forms.Select(attrs={
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


class socket(forms.Form):
    class Meta:
        fields = ['ids']
        widgets = {
            'ids': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'ids',
                    'id': "ids",

            })}

























