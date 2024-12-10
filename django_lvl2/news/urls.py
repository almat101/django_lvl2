from django.urls import path

from news.views import list_news, article_detail_view

urlpatterns = [
	path('list-news/', list_news, name="list-news"),
	path('articles/<int:pk>', article_detail_view , name="article_detail") # not recommended to expose pk outside
]
