from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from stars.models import Stars

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Stars.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'stars/index.html', context=context)


def about(request):
    return render(request, 'stars/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям</h1>\n<p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')
