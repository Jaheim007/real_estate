from django.shortcuts import render

def index(request): 
    return render(request, 'estateHTML\index.html')

def index2(request):
    return render(request, 'estateHTML\log.html')

def index3(request):
    return render(request, 'estateHTML\sign.html')
    

# Create your views here.
