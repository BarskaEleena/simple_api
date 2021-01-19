from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import random
from django.http import JsonResponse

# Create your views here.
def index(request):
    rand = ['a', 'b', 'c', 'd', 'e']
    #random.choice(foo))
    rand = random.choice(rand))
    data = [{"answer": rand}]
    return JsonResponse(data, safe=False)
    #return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
