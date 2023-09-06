from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TopPostsListView,
    CategoryListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('info/', views.info, name='blog-info'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category/Travel/', views.CategoryView, name='cat_travel'),
    path('category/Life/', views.CategoryView, name='cat_life'),
    path('category/Food/', views.CategoryView, name='cat_food'),
    path('category/#SeriousOnly/', views.CategoryView, name='cat_serious'),
    path('category/#Confessions/', views.CategoryView, name='cat_conf'),
    path('top-posts/', TopPostsListView.as_view(), name='top-posts'),
    path('discover/', CategoryListView.as_view(), name='discover')
]