from django.shortcuts import render

# Create your views here.
def en(request):
    return render(request, 'en.html')

def idn(request):
    return render(request, 'id.html')

def pack(request):
    return render(request, 'pack.html')

def packid(request):
    return render(request, 'packid.html')