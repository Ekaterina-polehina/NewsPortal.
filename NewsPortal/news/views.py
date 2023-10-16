from django.http import HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .filters import PostFilter
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView


class NewsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'flatpages/news.html'
    queryset = Post.objects.order_by('-date_create')
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class NewsSearch(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'flatpages/news_search.html'
    queryset = Post.objects.order_by('-date_create')
    context_object_name = 'news'
    #paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'flatpages/news_id.html'
    context_object_name = 'news_id'

class NewsCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'NE'
        return super().form_valid(form)

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    model = Post
    fields = ['author',  'title', 'content']
    template_name = 'flatpages/news_edit.html'


    def get_queryset(self):
        return super().get_queryset().filter(post_type = 'NE')




class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('news')

    def get_queryset(self):
        return super().get_queryset().filter(post_type = 'NE')



class ArticlesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/articles_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'AR'
        return super().form_valid(form)

class ArticlesUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    model = Post
    fields = ['author',  'title', 'content']
    template_name = 'flatpages/articles_edit.html'

    def get_queryset(self):
        return super().get_queryset().filter(post_type = 'AR')

class ArticlesDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'flatpages/articles_delete.html'
    success_url = reverse_lazy('news')

    def get_queryset(self):
        return super().get_queryset().filter(post_type = 'AR')



class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/news.html'
    model = Post
    form_class = PostForm
