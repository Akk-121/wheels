from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect, JsonResponse
from .models import CustomUser, buy, shop, questions
from django.contrib.auth.hashers import make_password
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
import pandas as pd
from django.db.models import Q


# Create your views here.
def index(request):
    sh = shop.objects.order_by('-id')
    return render(request, 'main/index.html')


# class shopListView(generic.ListView):
#     model = shop
#
#
# class shopDetailView(generic.DetailView):
#     # if request.method == 'POST':
#     #     pass
#     model = shop


# Странички про шины
def wheels(request):
    sh = shop.objects.filter(radio='Шины')[0:16]

    form = templateselect()
    long = len(sh)
    context = {
        'shop':sh,
        'form':form,
        'long': long,
    }
    return render(request, 'main/wheels.html', context)


def socket(request, pk:int):
    sh = shop.objects.filter(id=pk).first()
    if (request.session.get('socket') != None) and (request.session.get('socket_id') != None):
        x = request.session.get('socket')
        ids = request.session.get('socket_id')
        # print(ids)
        if sh.id not in ids:
            request.session['socket'] = x + [{'id': sh.id, 'name': sh.name,
                                              'diametr': sh.diametr, 'shirina':sh.shirina, 'profil': sh.profil,
                                              'manufacturer': sh.manufacturer, 'articul': sh.articul, 'price': sh.price}]
            request.session['socket_id'] = ids + [sh.id]
    else:
        request.session['socket'] = [{'id': sh.id, 'name': sh.name}]
        request.session['socket_id'] = [sh.id]

    next = request.META.get('HTTP_REFERER', None) or '/'
    response = HttpResponseRedirect(next)
    return response


def del_socket(request, pk:int):
    x = request.session.get('socket')
    ids = request.session.get('socket_id')
    try:
        delete = ids.index(pk)
        del x[delete]
        del ids[delete]
        request.session['socket'] = x
        request.session['socket_id'] = ids
    except: pass

    context = {
        'product': x
    }
    return HttpResponseRedirect("/socket")
    # return render(request, 'main/socket.html', context)


def socket_base(request):
    x = request.session.get('socket')
    # print(x)
    context = {
        'product': x
    }
    return render(request, 'main/socket.html', context)


def wheelsDetail(request, pk:int):
    sh = shop.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = questionsForm(request.POST)
        if form.is_valid():
            form.save()
            form = questionsForm()
            return render(request, 'main/wheelsdetail.html', {'wheel': sh, 'form': form})

    n = shop.objects.filter(id=pk).first()
    form = questionsForm(initial = dict(who=n))
    return render(request, 'main/wheelsdetail.html', {'wheel':sh, 'form': form})
#======================================


# Странички про диски
def disks(request):
    sh = shop.objects.filter(radio='Диски')

    if request.method == 'POST':
        form = templateselect_discks(request.POST)
        if form.is_valid():
            filt = {}
            if str(form.cleaned_data['diametr']) != 'Диаметр (R)':
                filt['diametr'] = str(form.cleaned_data['diametr'])
            if str(form.cleaned_data['shirina']) != 'Вылет (ЕТ)':
                filt['shirina'] = str(form.cleaned_data['shirina'])

            if str(form.cleaned_data['profil']) != 'Крепеж':
                filt['profil'] = str(form.cleaned_data['profil'])

            if str(form.cleaned_data['type']) != 'Тип':
                filt['type'] = str(form.cleaned_data['type'])

            if str(form.cleaned_data['manufacturer']) != 'Производитель':
                filt['manufacturer'] = str(form.cleaned_data['manufacturer'])

            try:
                sh1 = shop.objects.filter(diametr=filt['diametr'])
            except:
                sh1 = shop.objects.filter(radio='Диски')

            try:
                sh2 = sh1.filter(shirina=filt['shirina'])
            except:
                sh2 = sh1

            try:
                sh3 = sh2.filter(profil=filt['profil'])
            except:
                sh3 = sh2

            try:
                sh4 = sh3.filter(type=filt['type'])
            except:
                sh4 = sh3

            try:
                sh5 = sh4.filter(manufacturer=filt['manufacturer'])
            except:
                sh5 = sh4

            long = len(sh5)
            return render(request, 'main/disks.html', {'shop': sh5, 'form': form, 'long': long})
    form = templateselect_discks()
    long = len(sh)
    return render(request, 'main/disks.html', {'shop':sh, 'form':form, 'long': long})


def disksDetail(request, pk:int):
    sh = shop.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = questionsForm(request.POST)
        if form.is_valid():
            form.save()
            form = questionsForm()
            return render(request, 'main/wheelsdetail.html', {'wheel': sh, 'form': form})
    form = questionsForm()
    return render(request, 'main/disksdetail.html', {'wheel':sh, 'form': form})
#======================================


def about(request):
    return render(request, 'main/about.html')


@login_required()
@permission_required('shop.add_choice', login_url='logout')
def add(request):
    if request.method == 'POST':
        form = shopForm(request.POST or None,
                        files=request.FILES or None)
        if form.is_valid():
            form.save()

            form = shopForm()
            context = {
                'form1': form,
                'text' : 'Успех'
            }
            return render(request, 'main/add_wheels.html', context)
        else:
            context = {
                'form1': form,
                'text': 'Ошибка. Перепроверь свои поля'
            }
            return render(request, 'main/add_wheels.html', context)

    form = shopForm()
    context = {
        'form1': form
    }
    return render(request, 'main/add_wheels.html', context)


@login_required()
@permission_required('shop.add_choice', login_url='logout')
def add_any(request):
    def format_number(x, k=None):
        if type(x) is str:
            if x.isnumeric():
                return "{:,}".format(round(float(x), k)).replace(',', ' ').replace('.', ',')
            else:
                return x
        else:
            return "{:,}".format(round(x, k)).replace(',', ' ').replace('.', ',')

    if request.method == 'POST':
        form = fileForm(request.POST or None,
                        files=request.FILES or None,
                        )
        if form.is_valid():
            # form.save()
            df = pd.read_excel(request.FILES['file'], skiprows=2)
            df = df[df['Марка'].notna()]
            df.reset_index(drop=True, inplace=True)

            for i, row in df.iterrows():
                try:
                    product = shop()

                    product.season = row['зима/ лето']

                    setting = row['Размер'].split('/')
                    product.shirina = str(setting[1]).split('R')[0]
                    product.profil = setting[0]
                    product.diametr = str(setting[1]).split('R')[1]

                    product.manufacturer = row['Марка']

                    setting = str(row['Размер и Модель']).split()
                    model = ' '.join(setting[6:])
                    product.model_manufacturer = model

                    product.radio = 'Шины'
                    product.name = f"{row['Марка']} {model}"

                    product.price = format_number(str(round(int(row['В2В ']) + (int(row['В2В ']) /100) *30)))
                    product.speed = setting[4]
                    product.ves = setting[3]
                    product.articul = row['Артикул']

                    product.img = r'shop/default.png'

                    product.save()
                except: pass

            form = fileForm()
            context = {
                'form1': form,
                'text' : 'Успех'
            }
            return render(request, 'main/add_any.html', context)
        else:
            context = {
                'form1': form,
                'text': 'Ошибка. Перепроверь свои поля'
            }
            return render(request, 'main/add_any.html', context)

    form = fileForm()
    context = {
        'form1': form
    }
    return render(request, 'main/add_any.html', context)


def registration(request):
    if request.method == 'POST':
        form = registform(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(form.cleaned_data['email'])
            user.first_name = form.cleaned_data['name']
            user.number = form.cleaned_data['number']
            user.email = form.cleaned_data['email']
            user.password = make_password(form.cleaned_data['password1'], salt=None, hasher='default')
            user.save()
            form.save()
        else:
            context = {
                'form': form
            }
            return render(request, 'registration/registration.html', context)


    form = registform()
    context = {
        'form' : form
    }
    return render(request, 'registration/registration.html', context)

@login_required()
def account(request):
    username1 = request.user.username
    b = buy.objects.filter(user=username1)
    context = {'products':b}
    return render(request, 'main/account.html', context)


def anketa(request):
    qwe = questions.objects.all()
    context = {
        'qwe' : qwe
    }
    return render(request, 'main/anketa.html', context)

def order(request):
    buys = buy.objects.all()
    context = {
        'products': buys
    }
    return render(request, 'main/order.html', context)

class StatusApi(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            ans_id = request.GET.get('id')
            st = request.GET.get('st')
            if ans_id is not None:
                question = questions.objects.filter(id=ans_id).first()
                if question is not None:

                    question.status = st
                    question.save(update_fields=["status"])

                    return JsonResponse([f'{st}'], safe=False)
        return JsonResponse(['bad'], safe=False)


class ProductApi(View):
    def get(self, request, *args, **kwargs):
        st = request.GET.get('st')
        if st != 'new':
            len_shop = int(request.GET.get('long'))
        else:
            len_shop = 0

        diam = request.GET.get('diam')
        width_prof = request.GET.get('width_prof')
        height_prof = request.GET.get('height_prof')
        season = request.GET.get('season')
        manufacter = request.GET.get('manufacter')

        filt = {'radio': request.GET.get('radio')}
        if diam != 'Диаметр (R)':
            filt['diametr'] = diam
        if width_prof != 'Ширина профиля':
            filt['shirina'] = width_prof
        if height_prof != 'Высота профиля':
            filt['profil'] = height_prof
        if season != 'Сезон':
            filt['season'] = season
        if manufacter!= 'Производитель':
            filt['manufacturer'] = manufacter
        filt = Q(**filt)

        if len_shop is not None:
            if len(shop.objects.filter(filt)) > len_shop:
                if len(shop.objects.filter(filt)[len_shop:]) > 8:
                    sh = shop.objects.filter(filt)[len_shop:len_shop+8]
                else:
                    sh = shop.objects.filter(filt)[len_shop:]
                js = {}
                for i in range(len(sh)):
                    js[sh[i].id] = {'id':sh[i].id, 'name':sh[i].name, 'price':sh[i].price, 'diametr':sh[i].diametr, 'shirina':sh[i].shirina,
                                    'profil':sh[i].profil, 'img':str(sh[i].img), 'articul':sh[i].articul}
                return JsonResponse(['ok', js, len_shop + len(sh)], safe=False)
            else:
                return JsonResponse(['not object', f'К сожалению мы не можем загрузить еще {request.GET.get("radio")}. Проверьте свои фильтры и попробуйте еще раз.'], safe=False)
        return JsonResponse(['bad'], safe=False)


class StatusOrderApi(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            ans_id = request.GET.get('id')
            st = request.GET.get('st')
            if ans_id is not None:
                order = buy.objects.filter(id=ans_id).first()
                if order is not None:

                    order.status = st
                    order.save(update_fields=["status"])

                    return JsonResponse([f'{st}'], safe=False)
        return JsonResponse(['bad'], safe=False)






