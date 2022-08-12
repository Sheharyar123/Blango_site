from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
# Create your views here.

class SearchResultsListView(ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blog/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Blog.objects.filter(Q(author__username__icontains=query) | Q(title__icontains=query))

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'
    queryset = Blog.objects.filter(status=1)
    paginate_by = 3
    login_url = 'account_login'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    login_url = 'account_login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    fields = ('title', 'body', 'author', 'status',)
    success_url = reverse_lazy('blog:blog_list')
    login_url = 'account_login'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_edit.html'
    fields = ('title', 'body', 'status',)
    login_url = 'account_login'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')
    login_url = 'account_login'



        
    
    

