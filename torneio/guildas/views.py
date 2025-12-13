from django.shortcuts import render

# Create your views here.
def guildas(request):
    return render(
        request,
        'guildas/index.html'
    )