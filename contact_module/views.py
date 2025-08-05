from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from .forms import ContactUsForm
from .models import ContactUs


class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsForm()
        context = {
            'contact_form': contact_form
        }
        return render(request, 'contact_module/contact.html', context)

    def post(self, request):
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            user_full_name = contact_form.cleaned_data.get('full_name')
            user_email = contact_form.cleaned_data.get('email')
            user_phone = contact_form.cleaned_data.get('phone')
            user_subject = contact_form.cleaned_data.get('subject')
            user_message = contact_form.cleaned_data.get('message')
            new_user = ContactUs(
                full_name=user_full_name,
                email=user_email,
                phone=user_phone,
                subject=user_subject,
                message=user_message,
            )
            new_user.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد.')
            return redirect(reverse('contact'))
        context = {
            'contact_form': contact_form
        }
        return render(request, 'contact_module/contact.html', context)
