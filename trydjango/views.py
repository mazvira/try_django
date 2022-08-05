'''
To render Web HTML Web Pages
'''
import random
from urllib import response

from django.http import HttpResponse
from django.template.loader import render_to_string, get_template 
from articles.models import Article

def home_view(request, *args, **kwargs):
    '''
    Take in a request (Django sends request)
    Return HTML as a response (We p)
    '''
    name = "Justin"
    random_id = random.randint(1, 3)

    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "object_list": article_queryset
    }

    '''
     H1_STRING = f""" 
    <h1> {article_obj.title} (id: { article_obj.id }! ) </h1>
    """

    P1_STRING = f""" 
    <p> {article_obj.content} </p>
    """
    HTML_STRING = H1_STRING + P1_STRING
    '''
    HTML_STRING = render_to_string("home-view.html", context=context)

    tmpl = get_template("home-view.html")
    tmpl_string = tmpl.render(context)

    return HttpResponse(tmpl_string)
