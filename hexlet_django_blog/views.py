from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        url = reverse("articles:article", kwargs={"tags": "python", "article_id": 42})
        return redirect(url)


def about(request):
    return render(request, "about.html")
