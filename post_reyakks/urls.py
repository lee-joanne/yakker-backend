from django.urls import path
from post_reyakks import views


urlpatterns = [
    path('post_reyakks/', views.ListPostReyakks.as_view()),
    path('post_reyakks/<int:pk>', views.DetailPostReyakks.as_view())
]
