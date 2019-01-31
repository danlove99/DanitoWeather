from django.shortcuts import render
import importlib
from . import cardiff, london, dublin, glasgow, blackwood, manchester


def cardiffpage(request):
    Cardiff = cardiff.temp
    CardiffF = cardiff.fah
    CardiffSky = cardiff.skytemp
    return render(request, 'weather/cardiff.html', {'cardiff': Cardiff, 'cardiffF': CardiffF, 'cardiffSky': CardiffSky})


def londonpage(request):
    London = london.temp
    LondonF = london.fah
    LondonSky = london.skytemp
    return render(request, 'weather/london.html', {'london': London, 'londonF': LondonF, 'londonSky': LondonSky})


def dublinpage(request):
    Dublin = dublin.temp
    DublinF = dublin.fah
    DublinSky = dublin.skytemp
    return render(request, 'weather/dublin.html', {'dublin': Dublin, 'dublinF': DublinF, 'dublinSky': DublinSky})

def manchesterpage(request):
    Manchester = manchester.temp
    ManchesterF = manchester.fah
    ManchesterSky = manchester.skytemp
    return render(request, 'weather/manchester.html', {'manchester': Manchester, 'manchesterF': ManchesterF, 'manchesterSky': ManchesterSky})


def blackwoodpage(request):
    Blackwood = blackwood.temp
    BlackwoodF = blackwood.fah
    BlackwoodSky = blackwood.skytemp
    return render(request, 'weather/blackwood.html', {'blackwood': Blackwood, 'blackwoodF': BlackwoodF, 'blackwoodSky': BlackwoodSky})


def glasgowpage(request):
    Glasgow = glasgow.temp
    GlasgowF = glasgow.fah
    GlasgowSky = glasgow.skytemp
    return render(request, 'weather/glasgow.html', {'glasgow': Glasgow, 'glasgowF': GlasgowF, 'glasgowSky': GlasgowSky})


def index(request):
    London = london.temp
    Cardiff = cardiff.temp
    return render(request, 'weather/index.html', {'london': London, 'cardiff': Cardiff})

def index2(request):
    London = london.temp
    Cardiff = cardiff.temp
    return render(request, 'weather/index2.html', {'london': London, 'cardiff': Cardiff})