from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cardiff', views.cardiffpage, name='cardiff'),
    path('london', views.londonpage, name='london'),
    path('dublin', views.dublinpage, name='dublin'),
    path('glasgow', views.glasgowpage, name='glasgow'),
    path('blackwood', views.blackwoodpage, name='blackwood'),
    path('manchester', views.manchesterpage, name='manchester'),
    path('page2', views.index2, name='index2')
    ]