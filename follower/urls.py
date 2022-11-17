from django.urls import path
from follower import views


urlpatterns = [
    path('follower/', views.ListFollower.as_view()),
    path('follower/<int:pk>', views.DetailFollower.as_view())
]
