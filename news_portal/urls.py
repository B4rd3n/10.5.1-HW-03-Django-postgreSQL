from django.urls import path
from .views import NewsList, NewsDetailView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view()),
]
