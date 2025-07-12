from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.utils.crypto import get_random_string
from .forms import RegisterForm
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
            user_exist: CostumeUser = CostumeUser.objects.filter(email__iexact=user_email)
            if user_exist:
                register_form.add_error('email', 'ایمیل تکراری میباشد')
            else:
                new_user = CostumeUser(
                    email=user_email,
                    is_active=False,
                    username=user_email,
                    email_active_code=get_random_string(72),
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('home'))
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)
