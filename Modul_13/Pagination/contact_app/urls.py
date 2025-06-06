from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('success/', views.contact_success_view, name='contact_success'),
]