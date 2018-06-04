from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from plates.forms import RegistrationForm, UpdateProfileForm
from plates.models import Plate


def index(request):
    if request.method == 'POST':
        if "plate-number" in request.POST:
            try:
                plate = Plate.objects.get(plate=request.POST.get("plate-number"))
                messages.success(request, plate.plate + ' plakası bulundu.')
            except:
                messages.warning(request, 'Bu plaka sistemde kayıtlı değil!')
    if request.user.is_authenticated:
        update_profile_form = UpdateProfileForm(instance=request.user)
    else:
        register_form = RegistrationForm()
    plates = Plate.objects.all().filter(owner=request.user)
    return render(request, "index.html", locals())


def add_plate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if "new-plate-number" in request.POST:
                try:
                    plate = Plate.objects.create(plate=request.POST.get("new-plate-number"), owner=request.user)
                    messages.success(request, plate.plate + ' plakası eklendi.')
                except:
                    messages.warning(request, 'Bu plaka size kaydedilemedi.')
    else:
        messages.warning(request, 'Giriş Yapmamışsınız')
    return redirect('index')


def delete_plate(request, plate_number):
    if request.user.is_authenticated:
        try:
            plate = Plate.objects.get(plate=plate_number, owner=request.user)
            plate.delete()
            messages.success(request, plate.plate + ' plakası silindi.')
        except:
            messages.warning(request, 'Bu plaka kaydı silinemedi.')
    else:
        messages.warning(request, 'Giriş Yapmamışsınız')
    return redirect('index')


def send_notification_to(request, phone_number):
    """ Represented SMS Sender, Add Your Sender Here"""
    print(phone_number)
    messages.info(request, 'Kullanıcıya SMS gönderildi.')


def call(request, plate_number):
    if request.user.is_authenticated:
        try:
            plate = Plate.objects.get(plate=plate_number)
            send_notification_to(request, plate.owner.phone_number)
        except:
            messages.warning(request, 'Plaka kayıtlı değil')
    else:
        messages.warning(request, 'Giriş Yapmamışsınız')
    return redirect('index')


def login_controller(request):
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla giriş yaptınız')
        else:
            messages.warning(request, 'Lütfen bilgileri kontrol ediniz')
    return redirect('index')


def register_controller(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Hesap oluşturuldu ve hesaba giriş yapıldı!')
        else:
            messages.warning(request, 'Lütfen bilgileri kontrol ediniz')
    else:
        messages.warning(request, 'Lütfen bilgileri kontrol ediniz')
    return redirect('index')


def profile_update_controller(request):
    if request.method == 'POST':
        update_profile_form = UpdateProfileForm(request.POST, instance=request.user)
        if update_profile_form.is_valid():
            update_profile_form.save()
            messages.success(request, 'Bilgiler güncellendi!')
        else:
            messages.warning(request, 'Lütfen bilgileri kontrol ediniz')
    else:
        messages.warning(request, 'Lütfen bilgileri kontrol ediniz')
    return redirect('index')


def logout_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'Hesabınızdan çıkış yapıldı!')
        logout(request)
    return redirect('index')
