from django.shortcuts import render
from django.http import HttpResponse
import random as r
from .models import Cat


def getcats(request):
    catid = list(Cat.objects.values_list('id',flat = True))#facem o lista cu mate din database
    if len(catid)<2:
        return render(request,'lipsapisici.html')#nu am 2 pisici pe care sa le aleg=>nu aleg
    
    random_ids= r.sample(catid,2)

    pisica_1 = Cat.objects.get(id = random_ids[0])
    pisica_2  = Cat.objects.get(id = random_ids[1])

    context = {
        'cat1' : pisica_1,
        'cat2' : pisica_2,
    }

    return render(request,'home.html')
    

def leaderboard(request):
    cats = Cat.objects.all().order_by('-elo')
    return render(request, 'leaderboard.html', {'cats': cats})

def post_cat(request):
    return HttpResponse("leaderboard")
