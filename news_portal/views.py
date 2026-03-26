from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Post

class NewsList(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetailView(DetailView):
    model = Post
    template_name = 'single_news.html'
    context_object_name = 'single_news'
