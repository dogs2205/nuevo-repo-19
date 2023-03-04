from django.shortcuts import render

def index(request):
    return render(request, "SocialTravel/index.html")

# Create your views here.
