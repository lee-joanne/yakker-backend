from django.urls import path
from post import views


urlpatterns = [
    path('post/', views.ListPost.as_view()),
    path('post/<int:pk>', views.DetailPost.as_view())
]