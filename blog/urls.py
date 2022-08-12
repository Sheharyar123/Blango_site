from django.urls import path

from .views import (
    BlogListView, 
    BlogCreateView, 
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    SearchResultsListView
)   

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<slug:slug>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
