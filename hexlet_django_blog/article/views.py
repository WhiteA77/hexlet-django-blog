from django.shortcuts import render
from django.views import View


class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "app_name": "hexlet_django_blog.article",
            "description": "Страница собирается встроенным шаблонизатором Django.",
        }
        return render(request, "articles/index.html", context)