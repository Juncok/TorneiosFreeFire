from django.shortcuts import render

# Create your views here.
def criar_torneios(request):
    return render(
        request,
        'criar_torneios/index.html'
    )