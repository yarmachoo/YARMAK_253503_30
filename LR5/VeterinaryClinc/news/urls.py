from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('statistics/', views.StatisticsView.as_view(), name='statistics'),
    path('articles_statistics/', views.article_statistics_view, name='article-statistics')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


