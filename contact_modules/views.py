from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactUsForm


# Create your views here.
from django.urls import reverse


def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect('home_page')

    else:
        contact_form = ContactUsForm()

    return render(request, 'contact_modules/contact_us_page.html', {
        'contcat_form': contact_form
    })
