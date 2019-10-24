from django.shortcuts import render
from .forms import ContactForm



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm
    context = {
        'form':form
    }
    return render(request, 'form.html', context)
