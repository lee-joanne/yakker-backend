from django.urls import path
from comment_reyakks import views


urlpatterns = [
    path('comment_reyakks/', views.ListCommentReyakks.as_view()),
    path('comment_reyakks/<int:pk>', views.DetailCommentReyakks.as_view())
]