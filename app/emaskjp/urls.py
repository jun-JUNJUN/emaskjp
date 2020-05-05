from django.urls import path
from . import views

app_name = 'emaskjp'

urlpatterns = [
    path("forms/", views.formview, name="post_new"),
    path("confirm/", views.confirmview, name="post_confirm"),
    path("submit/", views.submitview, name="post_submit"),
    path("thanks/", views.thanksview, name="post_thanks"),
    path("supplyinput/", views.supplyformview, name="supplyinput"),
    path("supplysubmit/", views.supplysubmitview, name="supplysubmit"),
    path("", views.toppageview, name="toppage"),

]
