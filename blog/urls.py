from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),  
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
