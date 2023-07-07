from django.shortcuts import render


def web(request):
    return render(request, 'account/web.html')

