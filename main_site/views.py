from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from . import models

def index(request):
    i = 0
    posty = models.Post.objects.all().order_by("-published_date")
    popularne_posty = models.Post.objects.all().order_by("visit_counter").order_by("-published_date")
    context = {'posty' : posty, "popularne_posty" : popularne_posty, "i" : i}
    return render(request, 'main_site/index.html', context)
    
def details(request, post_id):
    post = models.Post.objects.filter(pk=int(post_id))
    context = {
        'post' : post
    }
    #return HttpResponse(str(post_id))
    return render(request, 'main_site/details.html', context)


def category_view(request, post_category):
    posty = models.Post.objects.filter(category = post_category).order_by("-published_date")
    return render(request, "main_site/category_view.html", {"posty" : posty, "category" : post_category.upper()})