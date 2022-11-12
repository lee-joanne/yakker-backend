from django.urls import path
from post import views


urlpatterns = [
    path('follower/', views.ListFollower.as_view()),
    path('follower/<int:pk>', views.DetailFollower.as_view())
]