from django.urls import path

from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)


app_name = "articles"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", ArticleFormCreateView.as_view(), name="create"),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="edit"),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="delete"),
    path("<int:id>/", ArticleView.as_view(), name="show"),
]
