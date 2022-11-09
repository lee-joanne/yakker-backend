from django.urls import path
from reyakks import views


urlpatterns = [
    path('reyakks/', views.ListReyakks.as_view()),
    path('reyakks/<int:pk>', views.DetailReyakks.as_view())
]