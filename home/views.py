from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text': 'Olá home, eu sou o home'
    }

    return render(
        request,
        'home/index.html',
        context,
    )
