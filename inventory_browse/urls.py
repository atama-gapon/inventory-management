from django.urls import path
from . import views


app_name = 'inventory_browse'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact_success/', views.ContactSuccessView.as_view(), name='contact_success')
]