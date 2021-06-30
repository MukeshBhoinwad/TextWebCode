# hi my name is Mukesh

from django.http import HttpResponse
from django.shortcuts import render
def entertainment(request):
    return render(request,'entertainment.html')





def index(request):

    return render(request, 'index.html')
    # return HttpResponse("Home")
    # return HttpResponse("Apna Page Ha Ye Toh!")
def analyze(request):
    #Get The Text
    djtext= request.POST.get('text','default')
    new=request.POST.get('New_Line_Remover','Off')

    remove=request.POST.get('about','Off')
    capt=request.POST.get('cap','off')
    #analyzed=djtext
    if remove=="on":
        punctuations ="""?…!.,–:;“‘[ ]_*!@#$%^&( )"""
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed,"muk":"Punctuation Removed"}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if capt=="on":
        analyzed=""
        for s in djtext:
            analyzed=analyzed+ s.upper()
        params = {'purpose': 'Capitalize All', 'analyzed_text':analyzed,"muk":"All Capitalize Done"}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    #if remove == "on" and capt == "on":
        #return HttpResponse("Chose Any one <br><a href='/'>BACK</a>")
    if new=="on":
        analyzed = ""
        for s in djtext:
            if s !="\n" and s!="\r":
                analyzed = analyzed + s
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed,"muk":"New Line Removed"}

        #return render(request, 'analyze.html', params)

    if remove!="on" and capt!="on" and new!="on":
        params = {"yourtext": "Please Click On CheckBox","muk":"Sorrry,Try again"}
        return render(request, 'analyze.html', params)

    #else:
        #params={"yourtext":"Please Click On CheckBox"}
    return render(request,'analyze.html',params)

    #return HttpResponse("HEllo MUkesh BHai    <a href='/'>BACK</a>")
#def about(request):
  #  djtext = request.GET.get('text', 'default')
  #  print(djtext)  # Analyaze Text
   # return HttpResponse("HEllo MUkesh BHai    <br><a href='/'>BACK</a>")
