from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by("-created_at")[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            "articles/create.html",
            context={"form": form},
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            messages.success(request, "Статья успешно создана")
            return redirect("articles:show", id=article.id)

        messages.error(request, "Исправьте ошибки формы")
        return render(
            request,
            "articles/create.html",
            context={"form": form},
        )


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        form = ArticleForm(instance=article)
        return render(
            request,
            "articles/update.html",
            context={
                "form": form,
                "article": article,
            },
        )

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            messages.success(request, "Статья успешно обновлена")
            return redirect("articles:show", id=article.id)

        messages.error(request, "Исправьте ошибки формы")
        return render(
            request,
            "articles/update.html",
            context={
                "form": form,
                "article": article,
            },
        )


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        article.delete()
        messages.success(request, "Статья удалена")
        return redirect("articles:index")
