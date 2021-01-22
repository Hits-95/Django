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
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitaliz = request.POST.get('capitaliz', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

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

        # bind analyze & remove new line
        for char in djtext:
            if char != '\n':
                analyzed += char

        params = {
            'purpose': 'Removed New Line',
            'analyzed_text': analyzed
        }

    # extra space remover
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char

        params = {
            'purpose': 'Removed NewLines',
            'analyzed_text': analyzed
        }
    # char counter
    elif charcounter == "on":
        analyzed = len(djtext)
        params = {
            'purpose': 'Charater Counter ',
            'analyzed_text': analyzed
        }

    else:
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)
