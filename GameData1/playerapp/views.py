from django.shortcuts import render
from django.http import HttpResponse

from playerapp.models import Player
from django.db.models import Count, Sum


def view_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        game = request.POST.get('game')
        score = request.POST.get('score')

        playObj = Player()
        playObj.name = name
        playObj.email = email
        playObj.country = country
        playObj.game = game
        playObj.score = score
        playObj.save()

        sports = Player.objects.all()
        return render(request, 'datatable.html', {'sports': sports})
    sports = Player.objects.all()
    return render(request, 'datatable.html', {'sports': sports})


def add_player(request):
    return render(request, 'addPlayer.html')


def edit_player(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        game = request.POST.get('game')
        score = request.POST.get('score')

        playObj = Player.objects.get(id=id)
        playObj.name = name
        playObj.email = email
        playObj.country = country
        playObj.game = game
        playObj.score = score
        playObj.save()

        sports = Player.objects.all()
        return render(request, 'datatable.html', {'sports': sports})
    else:
        sports = Player.objects.get(id=id)
        return render(request, 'editPlayer.html', {'sports': sports})


def delete_player(request, id):
    playObj = Player.objects.get(id=id)
    playObj.delete()
    sports = Player.objects.all()
    return render(request, 'datatable.html', {'sports': sports})


def overall(request):
    sports = Player.objects.all().values('name', 'email', 'country').annotate(total=Count('game')).annotate(sums=Sum('score')).order_by('-sums')
    return render(request, 'overall.html', {'sports': sports})
