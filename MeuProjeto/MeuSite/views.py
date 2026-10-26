from django.shortcuts import render

def home(request):
    """Página inicial do site: mostra os links para os currículos."""
    return render(request, 'home.html')
    
def index(request):
    """Renderiza o template index.html."""
    return render(request, 'index.html')


def meu_curriculo(request):
    """Renderiza o template meu-curriculo.html."""
    return render(request, 'meu-curriculo.html')