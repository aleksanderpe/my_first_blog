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
    