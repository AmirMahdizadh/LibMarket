from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView


class ContactUsView(FormView):
    template_name = 'contact_modules/contact_us_page.html'
    form_class = ContactUsForm
    success_url = '/contact_us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect('home_page')
    #
    #     return render(request, 'contact_modules/contact_us_page.html', {
    #         'contact_form': contact_form
    #     })
