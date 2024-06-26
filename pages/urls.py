from django.urls import path
from .views import AboutPageView, ContactsPageView

urlpatterns = [
    path("", AboutPageView.as_view(), name="about"),
    path("contact/", ContactsPageView.as_view(), name="contact"),
]
