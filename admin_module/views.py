from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from account_module.models import CustomUser
from .forms import EditProfileForm


class ProfileView(LoginRequiredMixin, View):
    template_name = 'admin_module/profile.html'
    login_url = 'login'

    def get(self, request):
        user = CustomUser.objects.filter(id=request.user.id).first()
        context = {
            'user': user,
        }
        return render(request, 'admin_module/profile.html', context)


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        edit_profile_form = EditProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
        })
        context = {
            'edit_profile_form': edit_profile_form,
            'user': user
        }
        return render(request, 'admin_module/edit_profile.html', context)

    def post(self, request):
        edit_profile_form = EditProfileForm(request.POST, request.FILES)
        user = request.user
        if edit_profile_form.is_valid():
            user.first_name = edit_profile_form.cleaned_data.get('first_name')
            user.last_name = edit_profile_form.cleaned_data.get('last_name')
            user.about_user = edit_profile_form.cleaned_data.get('about_user')
            user.avatar = edit_profile_form.cleaned_data.get('avatar')
            user.save()
            messages.success(request, 'اطلاعات شما با موفقیت تغییر یافت!')
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'admin_module/edit_profile.html', context)