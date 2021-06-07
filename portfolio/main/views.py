from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def projects(request):
    return render(request,'main/projects.html')

def languages(request):
    return render(request,'main/languages.html')

def experience(request):
    return render(request, 'main/experience.html')

def educations(request):
    return render(request, 'main/educations.html')

def achivements(request):
    return render(request, 'main/achivements.html')