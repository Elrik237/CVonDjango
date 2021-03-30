from django.urls import path
from . import views

urlpatterns = [
    path('', views.TimeNowView.as_view()),
]