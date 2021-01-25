from django.shortcuts import render

# our home page view
def index(request):    
    return render(request, 'index.html')
