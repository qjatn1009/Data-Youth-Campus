from django.urls import path
from . import views

urlpatterns = [
    path('resultmoive/', views.resultmoive , name ='resultmovie'),
    path('navermovie/', views.navermovie_star, name = 'navermovie'),
    path('main/', views.main, name='main'),
    path('keyword/', views.keyword, name='keyword'),
    path('resulkeyword/', views.resultkeyword, name='resultkeyword')
]