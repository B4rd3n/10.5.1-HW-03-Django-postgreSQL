from django.views.generic import ListView, DetailView, CreateView
from .filters import PostFilter
from .forms import PostForm

from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    filterset = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class NewsDetailView(DetailView):
    model = Post
    template_name = 'single_news.html'
    context_object_name = 'single_news'


class SearchNews(NewsList):
    template_name = 'search_news.html'


class CreateArticle(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_article.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.content_type = 'AT'
        return super().form_valid(form)
