from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param={'name':'tehreem','place':'sialkot'}
    return render(request,'index.html',param)
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in  punctuations:
                analyzed=analyzed + char
        params={'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext=analyzed
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
                analyzed=analyzed + char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed + char
        params={'purpose':'new line remover','analyzed_text':analyzed}
        djtext=analyzed
     
    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1] == " ":
               pass
            else:
                analyzed=analyzed + char
        params={'purpose':'extra Space remover','analyzed_text':analyzed}
    if extraspaceremover!="on" and newlineremover !="on" and fullcaps !="on" and removepunc !="on":
       return HttpResponse('error')
    return render(request,'analyze.html',params)