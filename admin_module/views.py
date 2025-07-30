from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import EditProfileForm, ChangePasswordForm
from account_module.models import CustomUser
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .mixins import AuthorRequiredMixin


class ProfileView(LoginRequiredMixin, View):
    template_name = 'admin_module/profile.html'
    login_url = 'login'

    def get(self, request):
        user = request.user
        edit_profile_form = EditProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
        })
        context = {
            'edit_profile_form': edit_profile_form,
            'user': user,
        }
        return render(request, 'admin_module/profile.html', context)

    def post(self, request):
        user = request.user
        edit_profile_form = EditProfileForm(request.POST, request.FILES)
        if edit_profile_form.is_valid():
            user.first_name = edit_profile_form.cleaned_data.get('first_name')
            user.last_name = edit_profile_form.cleaned_data.get('last_name')
            user.about_user = edit_profile_form.cleaned_data.get('about_user')
            user.avatar = edit_profile_form.cleaned_data.get('avatar')
            user.save()
            return redirect('profile')
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'admin_module/profile.html', context)


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        change_password_form = ChangePasswordForm
        context = {
            'change_password_form': change_password_form
        }
        return render(request, 'admin_module/change_password.html', context)

    def post(self, request):
        user: CustomUser = request.user
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            old_password = change_password_form.cleaned_data.get('old_password')
            new_password = change_password_form.cleaned_data.get('new_password')
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد!')
                update_session_auth_hash(request, user)
                return redirect(reverse('change_password'))
            else:
                change_password_form.add_error('old_password', 'رمز عبور فعلی نادرست است.')

        context = {
            'change_password_form': change_password_form
        }
        return render(request, 'admin_module/change_password.html', context)


