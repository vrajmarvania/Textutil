from django.http import HttpResponse
from django.shortcuts import render


def fun(request):
    return render(request, 'index.html')


def cun(request):
    aa = request.GET.get('text', 'default')
    lover = request.GET.get('lo', 'off')
    upe = request.GET.get('up', 'off')
    rem = request.GET.get('sr', 'off')
    rp = request.GET.get('rp', 'off')
    if rp == "on":
        an = ""
        pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in aa:
            if char not in pun:
                an = an + char

        params = {'ans': an}
        return render(request, 'prin.html', params)
    elif (rem == "on"):
        a1 = ''
        for char in aa:
            if not char == ' ':
                a1 = a1 + char
        params = {'ans': a1}
        return render(request, 'prin.html', params)
    elif (upe == "on"):
        a2 = ""
        for char in aa:
            a2 = a2 + char.upper()
        params = {'ans': a2}
        return render(request, 'prin.html', params)
    elif (lover == "on"):
        a3 = ""
        for char in aa:
            a3 = a3 + char.lower()
        params = {'ans': a3}
        return render(request, 'prin.html', params)
    else:
        return HttpResponse('ERROR')
