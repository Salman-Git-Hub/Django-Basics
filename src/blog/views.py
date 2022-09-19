from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article


# Create your views here.

# templates: <appname>/<modelname>_<view>.html

# Class Based Views
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # Optional
    # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")  # get the url parameter
        return get_object_or_404(Article, id=id_)

