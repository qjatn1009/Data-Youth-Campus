from django.urls import path
from . import views

urlpatterns = [
    path('regform/', views.student_regform, name = 'regform'), #데이터를 받는 곳
    path('register/', views.student_register, name = 'register'), # 데이터를 등록하는 곳
    path('search/', views.student_search, name = 'search'),
    path('<str:name>/modiform/', views.student_modiform, name = 'modiform'),
    path('modify/', views.student_modify, name = 'modify'),
    path('<str:name>/delete/', views.student_delete, name = 'delete'),
    path('<str:name>/detail/', views.student_detail, name = 'detail')
]