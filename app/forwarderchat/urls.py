from django.urls import path
from . import views

app_name = 'forwarderchat'

urlpatterns = [
    path("", views.home, name="home"),
    path("listtext/", views.listRFItext, name="listRFItext"),
    path("list/", views.listRFI, name="listRFI"),
    path('detail/<int:RFI_id>/', views.detailRFI, name="detail"),
    path('testforminput/', views.testforminput, name="testforminput"),
    path('inputrfi/', views.inputrfi, name="inputrfi")
]
