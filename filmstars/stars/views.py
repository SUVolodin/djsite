from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from stars.models import Stars

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Stars.objects.all()
    return render(request, 'stars/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'stars/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям</h1>\n<p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

