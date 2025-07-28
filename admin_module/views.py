from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

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
        edit_profile_form = EditProfileForm()
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'admin_module/edit_profile.html', context)

    def post(self, request):
        edit_profile_form = EditProfileForm(request.POST)
        if edit_profile_form.is_valid():
            pass
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'admin_module/edit_profile.html', context)
