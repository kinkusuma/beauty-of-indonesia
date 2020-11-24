from django.shortcuts import render

# Create your views here.
def en(request):
    return render(request, 'en.html')

def id(request):
    return render(request, 'id.html')