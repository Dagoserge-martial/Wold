from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    articleAccueil = Article.objects.filter(article_acueil=True)
    categorieList = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    data = {
        'articleAccueil': articleAccueil,
        'categorieList': categorieList,
        'article_all': article_all
    }
    return render(request, 'pages/index.html',data)

def categorie(request):
    categorie = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    data = {
        'categorie': categorie,
        'article_all': article_all,
    }
    print(id)
    return render(request, 'pages/categorie.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def regular(request):
    return render(request, 'pages/regular.html')

def blogSingle(request, id):
    try:
        article = Article.objects.get(pk=id)
    except:
        return redirect('home')
        
    data = {
        'article': article,
    }
    print(id)
    return render(request, 'pages/blogSingle.html', data)