from django.shortcuts import render
from .models import premier_league

# Create your views here.
def Home(request):
    return render(request, 'blog/Home.html', {})

def league_stats(request):
    return render(request, 'blog/league_stats.html',{})

def pre(request):
    all_team = premier_league.objects.all().order_by('-point')
    i=1
    for team in all_team:
        team.rank = i
        if(i==1):
            team.idx = 'uefac'
        elif(i==2):
            team.idx = 'uefac2'
        elif(i==3):
            team.idx = 'uefac3'
        elif(i==4):
            team.idx = 'uefac4'
        elif(i==5):
            team.idx = 'uefau'
        elif(i==6):
            team.idx = 'uefau'
        elif(i==18):
            team.idx = 'relegation'
        elif(i==19):
            team.idx = 'relegation'
        elif(i==20):
            team.idx = 'relegation'
        i=i+1
    league = {'all_team':all_team}
    return render(request, 'blog/league_stats_pre.html',league)