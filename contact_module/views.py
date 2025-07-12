from django.views.generic import View
from django.shortcuts import render
from .forms import ContactUsForm


class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsForm()
        context = {
            'contact_form': contact_form
        }
        return render(request, 'contact_module/contact.html', context)
