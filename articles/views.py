import imp
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article

# Create your views here.

def article_search_view(request):
    context = {}
    print(request.GET)
    query_dict = request.GET
    
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    atricle_obj = None

    if query is not None:
        try:
            atricle_obj = Article.objects.get(id=query)
        except:
            atricle_obj = None
    
    context = {
        "object": atricle_obj, 
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request, id=None):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save() 
        context['form'] = ArticleForm()

    return render(request, "articles/create.html", context=context)

'''
old version (bad version of the code)
def article_create_view(request, id=None):
    form = ArticleForm()
    context = {
        "form": form
    }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')

            article_object = Article.objects.create(title=title, content=content)
        
            context['object'] = article_object
            context['created'] = True
        

    return render(request, "articles/create.html", context=context)    
'''

def article_detail_view(request, id=None):
    atricle_obj = None
    if id is not None:
        atricle_obj = Article.objects.get(id=id)
    context = {
        "object": atricle_obj, 
    }
    return render(request, "articles/detail.html", context=context)