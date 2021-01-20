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
    capitaliz = request.GET.get('capitaliz', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')

    # check for panctuation mark
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
    # make it as capitaliz
    elif capitaliz == "on":

        analyzed = djtext.upper()

        params = {
            'purpose': 'Change to Upper-Case',
            'analyzed_text': analyzed
        }
    # remve new line
    elif newlineremover == "on":
        analyzed = ""
        params = {
            'purpose': 'Removed New Line',
            'analyzed_text': analyzed
        }

    else:
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)
