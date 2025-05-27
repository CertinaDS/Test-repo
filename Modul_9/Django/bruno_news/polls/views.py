from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Ну здравствуй, мир. Вы находитесь в индексе опросов общественного мнения.")
# Create your views here.
