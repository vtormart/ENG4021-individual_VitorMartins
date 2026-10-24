from django.shortcuts import render

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'home.html')


from django.shortcuts import render



def index(request):
   
    return render(request, 'index.html')


def meu-curriculo(request):
    
    return render(request, 'meu-curriculo.html')