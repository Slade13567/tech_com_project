from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def login_page(request):
    return render(request, 'main/login.html')

def quizz(request):
    return render(request, 'main/quizz.html')

def skills(request):
    return render(request, 'main/skills.html')