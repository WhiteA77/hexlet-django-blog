from django.shortcuts import render

def index(request):
    context = {
        "app_name": "hexlet_django_blog.article",  # название приложения
        "description": "Страница собирается встроенным шаблонизатором Django.",
    }
    return render(request, "articles/index.html", context)
