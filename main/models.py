from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    text = models.TextField('Комментарий', blank=True, null=True)
    # add additional fields in here


class shop(models.Model):
    diametr = models.CharField('Диаметр', max_length=10)
    shirina = models.CharField('Ширина / Вылет', max_length=10, help_text='Для шин-ширина, для дисков-вылет')
    profil = models.CharField('Профиль / Крепеж', max_length=10, help_text='Для шин-профиль, для дисков-крепеж')
    manufacturer = models.TextField('Производитель', max_length=50, help_text='Выберите производителя', null=True, blank=True)
    model_manufacturer = models.TextField('Модель', max_length=50, help_text='Выберите модель', null=True, blank=True)
    orr0 = (
        ('Лето', 'Лето'),
        ('Зима Шип', 'Зима Шип'),
        ('Зима Не Шип', 'Зима Не Шип')
    )
    season = models.CharField('Сезон', max_length=10, help_text='Сезонность', choices=orr0, null=True, blank=True)

    orr = (
        ('Шины', 'Шины'),
        ('Диски', 'Диски')
    )
    radio = models.CharField('Категория', max_length=10, choices=orr, null=True, blank=True)
    name = models.TextField('Название', max_length=50, help_text='Введите название', default='', null=True, blank=True)
    text = models.TextField('Описание', null=True)
    price = models.CharField('Цена', max_length=10, null=True, blank=True)
    ostatok = models.CharField('Остаток', max_length=10, null=True, blank=True)

    speed = models.TextField('Индекс скорости', max_length=25, null=True, blank=True)
    ves = models.TextField('Индекс нагрузки', max_length=25, null=True, blank=True)

    img = models.ImageField('Изображение', upload_to='shop/', null=True)
    # img = models.FileField('Изображения', upload_to='shop/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']

class regist(models.Model):
    username = models.CharField('Username', max_length=50)
    name= models.CharField('Name', max_length=50)
    email = models.EmailField('e-mail')
    password1 = models.CharField('Пароль', max_length=50)
    password2 = models.CharField('Повтор пароля', max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class questions(models.Model):
    about = models.TextField('Описание')
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    number = models.CharField('Телефон', max_length=50, blank=True, null=True)
    email = models.EmailField('e-mail')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'


class buy(models.Model):
    user = models.CharField('Username', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    product = models.CharField('Что купил', max_length=50)
    price = models.CharField('Цена', max_length=50, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class select(models.Model):
    diametr = models.CharField('Диаметр', max_length=50)
    shirina = models.CharField('Ширина', max_length=50)
    profil = models.CharField('Высота', max_length=50)
    season = models.CharField('Сезон', max_length=50)
    who = models.CharField('Производитель', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.who

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выбор'