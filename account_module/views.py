from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.utils.translation.trans_real import reset_cache
from django.views.generic import View

from .forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from .models import CustomUser


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
            user_exist: CustomUser = CustomUser.objects.filter(email__iexact=user_email).first()
            if user_exist and user_exist.is_active == True:
                register_form.add_error('email', 'با این ایمیل قبلا ثبت نام شده است!')
            elif user_exist and user_exist.is_active == False:
                register_form.add_error('email', 'حساب شما از قبل ایجاد شده! برای فعالسازی ایمیل خود را بررسی کنید!')
            else:
                new_user = CustomUser(
                    email=user_email,
                    is_active=False,
                    username=user_email,
                    email_active_code=get_random_string(72),
                )
                new_user.set_password(user_password)
                new_user.save()
                # TODO: send verification email
                messages.success(request, 'حساب شما ایجاد شد! برای فعالسازی، ایمیل خود را بررسی کنید!')
                return redirect(reverse('register'))
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: CustomUser = CustomUser.objects.filter(email_active_code__iexact=email_active_code).first()
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
            user: CustomUser = CustomUser.objects.filter(email__iexact=user_email).first()
            if user is None:
                login_form.add_error('email', 'نام کاربری یا کلمه عبور اشتباه است.')
            elif not user.is_active:
                login_form.add_error('email', 'حساب شما فعال نشده است، ایمیل خود را بررسی کنید.')
            elif not user.check_password(user_password):
                login_form.add_error('email', 'نام کاربری یا کلمه عبور اشتباه است.')
            else:
                login(request, user)
                return redirect(reverse('home'))

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ForgotPasswordView(View):
    def get(self, request):
        forgot_password_form = ForgotPasswordForm()
        context = {
            'forgot_password_form': forgot_password_form
        }
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request):
        forgot_password_form = ForgotPasswordForm(request.POST)
        if forgot_password_form.is_valid():
            user_email = forgot_password_form.cleaned_data.get('email')
            user_exist: CustomUser = CustomUser.objects.filter(email__iexact=user_email).first()
            if not user_exist:
                messages.success(request, message='در صورتی که حسابی با این ایمیل وجود داشته باشد، لینک بازیابی رمز عبور برایتان ارسال می‌شود.')
            else:
                # TODO: send forget password email
                pass
                messages.success(request, message='در صورتی که حسابی با این ایمیل وجود داشته باشد، لینک بازیابی رمز عبور برایتان ارسال می‌شود.')
                return redirect(reverse('login'))
        context = {
            'forgot_password_form': forgot_password_form
        }
        return render(request, 'account_module/forgot_password.html', context)


class ResetPasswordView(View):
    def get(self, request, email_active_code):
        user_exist: CustomUser = CustomUser.objects.filter(email_active_code__iexact=email_active_code)
        if not user_exist:
            messages.error(request, 'لینک بازیابی رمز عبور نامعتبر یا منقضی شده است. لطفاً مجدداً درخواست بازیابی رمز عبور ارسال کنید.')
            return redirect(reverse('forgot_password'))
        context = {
            'reset_password_form': ResetPasswordForm()
        }
        return render(request, 'account_module/reset_password.html', context)
