from django.shortcuts import render, redirect
from .models import CustomUser, buy, shop
from django.contrib.auth.hashers import make_password
from .forms import shopForm, registform, questionsForm, templateselect
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required


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
    sh = shop.objects.filter(radio='Шины')#[0:13]
    if request.method == 'POST':
        form = templateselect(request.POST)
        if form.is_valid():
            filt = {}
            if str(form.cleaned_data['diametr']) != 'Диаметр (R)':
                filt['diametr'] = str(form.cleaned_data['diametr'])
            if str(form.cleaned_data['shirina']) != 'Ширина профиля':
                filt['shirina'] = str(form.cleaned_data['shirina'])

            profil = form.cleaned_data['profil']
            season = form.cleaned_data['season']
            manufacturer = form.cleaned_data['manufacturer']

            try:
                sh1 = shop.objects.filter(diametr=filt['diametr'])
            except:
                sh1 = shop.objects.filter(radio='Шины')

            try:
                sh2 = sh1.filter(shirina=filt['shirina'])
            except:
                sh2 = sh1

            return render(request, 'main/wheels.html', {'shop': sh2, 'form': form})
    form = templateselect()
    return render(request, 'main/wheels.html', {'shop':sh, 'form':form})


def wheelsDetail(request, pk:int):
    sh = shop.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = questionsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/wheelsdetail.html', {'wheel': sh, 'form': form})
    form = questionsForm()
    return render(request, 'main/wheelsdetail.html', {'wheel':sh, 'form': form})
#======================================


# Странички про диски
def disks(request):
    sh = shop.objects.filter(radio='Диски')
    return render(request, 'main/disks.html', {'shop':sh})


def disksDetail(request, pk:int):
    sh = shop.objects.filter(id=pk).first()
    return render(request, 'main/disksdetail.html', {'wheel':sh})
#======================================


def about(request):
    return render(request, 'main/about.html')


@login_required()
@permission_required('shop.add_choice', login_url='logout')
def add(request):
    if request.method == 'POST':
        form = shopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = shopForm()
    context = {
        'form1': form
    }
    return render(request, 'main/add.html', context)


def registration(request):
    if request.method == 'POST':
        form = registform(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(form.cleaned_data['username'])
            user.first_name = form.cleaned_data['name']
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