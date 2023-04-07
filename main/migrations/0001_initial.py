# Generated by Django 2.1.5 on 2023-04-04 17:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='Username')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('product', models.CharField(max_length=50, verbose_name='Что купил')),
                ('price', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цена')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='Описание')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='regist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('password1', models.CharField(max_length=50, verbose_name='Пароль')),
                ('password2', models.CharField(max_length=50, verbose_name='Повтор пароля')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametr', models.CharField(max_length=50, verbose_name='Диаметр')),
                ('shirina', models.CharField(max_length=50, verbose_name='Ширина')),
                ('profil', models.CharField(max_length=50, verbose_name='Высота')),
                ('season', models.CharField(max_length=50, verbose_name='Сезон')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Выбор',
                'verbose_name_plural': 'Выбор',
            },
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametr', models.CharField(max_length=10, verbose_name='Диаметр')),
                ('shirina', models.CharField(help_text='Для шин-ширина, для дисков-вылет', max_length=10, verbose_name='Ширина / Вылет')),
                ('profil', models.CharField(help_text='Для шин-профиль, для дисков-крепеж', max_length=10, verbose_name='Профиль / Крепеж')),
                ('manufacturer', models.TextField(blank=True, help_text='Выберите производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('model_manufacturer', models.TextField(blank=True, help_text='Выберите модель', max_length=50, null=True, verbose_name='Модель')),
                ('season', models.CharField(blank=True, choices=[('Лето', 'Лето'), ('Зима Шип', 'Зима Шип'), ('Зима Не Шип', 'Зима Не Шип')], help_text='Сезонность', max_length=10, null=True, verbose_name='Сезон')),
                ('radio', models.CharField(blank=True, choices=[('Шины', 'Шины'), ('Диски', 'Диски')], max_length=10, null=True, verbose_name='Категория')),
                ('name', models.TextField(blank=True, default='', help_text='Введите название', max_length=50, null=True, verbose_name='Название')),
                ('text', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.CharField(blank=True, max_length=10, null=True, verbose_name='Цена')),
                ('ostatok', models.CharField(blank=True, max_length=10, null=True, verbose_name='Остаток')),
                ('speed', models.TextField(blank=True, max_length=25, null=True, verbose_name='Индекс скорости')),
                ('ves', models.TextField(blank=True, max_length=25, null=True, verbose_name='Индекс нагрузки')),
                ('img', models.ImageField(null=True, upload_to='shop/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Товары',
                'ordering': ['-id'],
            },
        ),
    ]
