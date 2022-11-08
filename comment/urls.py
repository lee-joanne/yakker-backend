from django.urls import path
from comment import views


urlpatterns = [
    path('comment/', views.ListComment.as_view()),
    path('comment/<int:pk>', views.DetailComment.as_view())
]