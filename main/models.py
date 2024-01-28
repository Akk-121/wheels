from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import RegexValidator
import uuid

class CustomUser(AbstractUser):
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField('Комментарий', blank=True, null=True)
    number = models.CharField('Номер телефона', max_length=18, null=True)
    # test = models.CharField('Тестовое поле', max_length=18, null=True)
    # add additional fields in here

class shop(models.Model):
    diametr = models.CharField('Диаметр', max_length=10)
    shirina = models.CharField('Ширина / Вылет (ЕТ)', max_length=10, help_text='Для шин-ширина, для дисков-вылет')
    profil = models.CharField('Профиль / Крепеж', max_length=10, help_text='Для шин-профиль, для дисков-крепеж')
    manufacturer = models.TextField('Производитель', max_length=50, help_text='Выберите производителя')

    type_list = (
        ('Литой', 'Литой'),
        ('Штампованный', 'Штампованный'),
        ('Кованый', 'Кованый')
    )
    type = models.CharField('Тип диска', max_length=50, help_text='Выберите тип', choices=type_list, null=True, blank=True)

    model_manufacturer = models.TextField('Модель', max_length=50, help_text='Выберите модель', null=True, blank=True)

    orr0 = (
        ('Лето', 'Лето'),
        ('Зима Шип', 'Зима Шип'),
        ('Зима Не Шип', 'Зима Не Шип')
    )
    season = models.CharField('Сезон', max_length=15, help_text='Сезонность', choices=orr0, null=True, blank=True)

    orr = (
        ('Шины', 'Шины'),
        ('Диски', 'Диски')
    )

    radio = models.CharField('Категория', max_length=10, choices=orr, null=True, blank=True)
    name = models.TextField('Название', max_length=50, help_text='Введите название', default='', null=True, blank=True)
    text = models.TextField('Описание', null=True)
    price = models.CharField('Цена', max_length=10, null=True, blank=True)
    # price_num = int(str(price).replace(' ', ''))
    ostatok = models.CharField('Остаток', max_length=10, null=True, blank=True)

    speed = models.TextField('Индекс скорости', max_length=25, null=True, blank=True)
    ves = models.TextField('Индекс нагрузки', max_length=25, null=True, blank=True)

    # img = models.ImageField('Изображение', upload_to='shop/', null=True)
    img = models.FileField('Изображения', upload_to='shop/', blank=True, null=True)
    articul = models.TextField('Артикул', max_length=25, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']


class files(models.Model):
    name = models.TextField('Название', max_length=50, help_text='Введите название', default='excel file', null=True, blank=True)
    file = models.FileField('Excel', upload_to='file/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-id']


class regist(models.Model):
    # username = models.CharField('Username', max_length=50, null=True, blank=True)
    name= models.CharField('Name', max_length=50)

    # phone_regex = RegexValidator(regex=r'^\+?1?\d{11,18}$',
    #                              message="Номер телефона должен быть формата: '+7 (123) 456 78 90'. Допускается до 18 символов.")
    # number = models.CharField(validators=[phone_regex], max_length=18, null=True)  # Validators should be a list
    number = models.CharField('Номер телефона', max_length=18, null=True)

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
    who = models.TextField('Какой товар', blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    number = models.CharField('Телефон', max_length=50, blank=True, null=True)
    email = models.EmailField('e-mail')
    time = models.DateTimeField(default=timezone.now)

    orr = (
        ('new', 'new'),
        ('work', 'work'),
        ('close', 'close')
    )

    status = models.CharField('Статус', max_length=30, choices=orr, default='new', blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        ordering = ['-id']


class buy(models.Model):
    user = models.CharField('Username', max_length=50)

    number = models.CharField('Номер телефона', max_length=18, null=True)
    email = models.EmailField('e-mail', blank=True, null=True)

    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)

    product = models.CharField('Что купил', max_length=50)
    price = models.CharField('Цена', max_length=50, blank=True, null=True)

    articul = models.CharField('Артикул', max_length=25, null=True, blank=True)
    ostatok = models.CharField('Количество', max_length=10, null=True, blank=True)

    id_product = models.CharField('Айдишник товара', max_length=5, null=True, blank=True)
    orr = (
        ('Создан', 'Создан'),
        ('Комплектуется', 'Комплектуется'),
        ('В пути', 'В пути'),
        ('Ожидает получения', 'Ожидает получения'),
        ('Выдан', 'Выдан'),
    )
    status = models.CharField('Статус заказа', max_length=50, choices=orr, default='Создан')

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
