from django.shortcuts import render

# Create your views here.
def About(request):
    return render (request, 'members/index.html')