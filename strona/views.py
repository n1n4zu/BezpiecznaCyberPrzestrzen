from django.shortcuts import render


def base(request):
    return render(request, 'strona/base.html', {})


def glowna(request):
    return render(request, 'strona/glowna.html', {})


def posty(request):
    return render(request, 'strona/posty.html', {})


def nauka(request):
    return render(request, 'strona/nauka.html', {})


def kontakt(request):
    return render(request, 'strona/kontakt.html', {})


def error_404_view(request, exception):
    data = {"name": 'BezpiecznaCyberPrzestrzeń'}
    return render(request, 'strona/404.html', data)


def error_500_view(request):
    data = {"name": 'BezpiecznaCyberPrzestrzenie'}
    return render(request, 'strona/500.html', data)

