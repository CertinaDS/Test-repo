from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Главная страница</h1>
        <p><a href="/contact/">Перейти к контактной форме</a></p>
        <p><a href="/admin/">Администрирование</a></p>
    """)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('contact_app:contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'contact_app/contact_form.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_app/contact_success.html')