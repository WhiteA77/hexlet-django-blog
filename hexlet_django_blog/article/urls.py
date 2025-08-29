from django.urls import path
from hexlet_django_blog.article.views import ArticleIndexView, index

app_name = "articles"

urlpatterns = [
    path("", ArticleIndexView.as_view(), name="index"),
    path("<str:tags>/<int:article_id>/", index, name="article"),
]
