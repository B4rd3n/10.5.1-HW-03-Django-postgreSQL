from django.urls import path
from .views import NewsList, NewsDetailView, SearchNews, CreateArticle

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('search/', SearchNews.as_view(), name='news_search'),
    path('articles/create/', CreateArticle.as_view(), name='articles_create'),
]
