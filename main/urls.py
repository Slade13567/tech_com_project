from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('quizz/', views.quizz, name='quizz'),
    path('skills/', views.skills, name='skills'),
]