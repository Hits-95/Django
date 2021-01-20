from django.http import HttpResponse
from django.shortcuts import render

# video - 6
# def index(request):
#     return HttpResponse("<h2> Hitesh Ahire ... </h2> <a href = 'https://github.com/Hits-95/Django/blob/hitesh/TextData/textdata/textdata/views.py'> hitesh </a>")
#
# def about_hits(request):
#     return HttpResponse("<h2> About Hitesh Ahire ... </h2>")

# video -7


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h2 style = 'color : green', > Hitesh Ahire </h2>")


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:\'",<>./?@#$%^&*_~'''

        analyzed = ""

        # bind analyze
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
