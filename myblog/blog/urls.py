from django.contrib import admin
from django.urls import path
from . import views
from .views import PostDetailView,PostCreateView,PostUpdateView,PostDeleteview
urlpatterns = [
    
    path('',views.blog_view,name="blog-home"),
    path('about/',views.about_view,name='blog-about'),
    path('post/',PostCreateView.as_view(),name='post-create'),
    path('detail/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('detail/delete/<int:pk>',PostDeleteview.as_view(),name='post-delete'),
    path('update/<int:pk>',PostUpdateView.as_view(),name='post-update')
]
