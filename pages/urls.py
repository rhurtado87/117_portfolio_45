from django.urls import path
from django.contrib import admin
from pages.views import about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about, name='about'),
    path('contact', contact, name ='contact')

]
