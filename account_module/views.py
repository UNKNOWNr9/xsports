from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.views.generic import View

from .forms import RegisterForm, LoginForm
from .models import CostumeUser


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user_exist: CostumeUser = CostumeUser.objects.filter(email__iexact=user_email).first()
            if user_exist and user_exist.is_active == True:
                register_form.add_error('email', 'این ایمیل قبلا ثبت نام شده است!')
            elif user_exist and user_exist.is_active == False:
                register_form.add_error('email', 'حساب شما از قبل ایجاد شده! برای فعالسازی ایمیل خود را بررسی کنید!')
            else:
                new_user = CostumeUser(
                    email=user_email,
                    is_active=False,
                    username=user_email,
                    email_active_code=get_random_string(72),
                )
                new_user.set_password(user_password)
                new_user.save()
                messages.success(request, 'حساب شما ایجاد شد! برای فعالسازی، ایمیل خود را بررسی کنید!')
                return redirect(reverse('register'))
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: CostumeUser = CostumeUser.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                messages.success(request, 'حساب کاربری شما فعال شد! فقط کافیست وارد شوید!')
                return redirect(reverse('login'))
            else:
                messages.success(request, 'حساب کاربری شما فعال شد! فقط کافیست وارد شوید!')
                return redirect(reverse('login'))
        messages.error(request, 'ایمیلی یافت نشد، ثبت نام کنید!')
        return redirect(reverse('login'))


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: CostumeUser = CostumeUser.objects.filter(email__iexact=user_email).first()
            if user is None:
                login_form.add_error(None, 'نام کاربری یا کلمه عبور اشتباه است.')
            elif not user.is_active:
                login_form.add_error(None, 'حساب شما فعال نشده است، ایمیل خود را بررسی کنید.')
            elif not user.check_password(user_password):
                login_form.add_error(None, 'نام کاربری یا کلمه عبور اشتباه است.')
            else:
                login(request, user)
                return redirect(reverse('home'))

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)
