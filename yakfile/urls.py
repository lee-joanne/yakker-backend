from django.urls import path
from yakfile import views


urlpatterns = [
    path('yakfile/', views.ListYakfile.as_view()),
    path('yakfile/<int:pk>', views.DetailYakfile.as_view())
]
