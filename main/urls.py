from django.urls import path

from .views import SendMailPage

urlpatterns = [
    path('', SendMailPage.as_view(), name="mail")
]
