from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/edit/', views.UpdatePostView.as_view(), name='update_post'),
    path('post/<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]
