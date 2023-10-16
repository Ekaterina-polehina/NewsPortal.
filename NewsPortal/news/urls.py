from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete,
    ArticlesCreate, ArticlesUpdate, ArticlesDelete, ProtectedView
)

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/search/', NewsSearch.as_view(), name='news_search'),

    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
    path('news/', ProtectedView.as_view(), name='news'),
]
