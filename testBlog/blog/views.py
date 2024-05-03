from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super(ShowNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница сайта'
        return context


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')


    def get_context_data(self, **kwargs):
        context = super(UserAllNewsView, self).get_context_data(**kwargs)
        context['title'] = f'Статьи пользователя {self.kwargs.get("username")}'
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context
    

class UpdateNewsView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        context = super(UpdateNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Обновление статьи'
        context['btn_text'] = 'Обновить статью' 
        return context
    

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False
    
    
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
    

class DeleteNewsView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'blog/delete-news.html'
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


class CreateNewsView(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        context = super(CreateNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['btn_text'] = 'Добавить статью' 
        return context

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Контакты'})
