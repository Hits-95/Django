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


def removepunc(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse("remove punc")
