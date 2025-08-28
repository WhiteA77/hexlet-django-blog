from django.urls import path
from hexlet_django_blog.article.views import ArticleIndexView

app_name = "articles"

urlpatterns = [
    path("", ArticleIndexView.as_view(), name="index"),
]