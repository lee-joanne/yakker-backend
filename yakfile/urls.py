from django.urls import path
from yakfile import views


urlpatterns = [
    path('yakfile/', views.ListYakfile.as_view())
]