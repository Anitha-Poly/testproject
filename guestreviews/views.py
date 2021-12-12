from django.shortcuts import render
from django.http import HttpResponse
from .models import admini,library,guest,public,Book
from .forms import adminiForm,libraryForm,guestForm,publicForm,bookForm

# Create your views here.
def home(request):
    return render(request,"main.html")
def admini(request):
    gf = adminiForm
    if request.method == "POST":
        gf = adminiForm(request.POST, request.FILES)
        if gf.is_valid():

            gf.save()
        else:
            HttpResponse("invalid")
    return render(request,"administrator.html",{'key':gf})
def guest(request):
    af = guestForm
    if request.method == "POST":
        af= guestForm(request.POST, request.FILES)
        if af.is_valid():
            af.save()
        else:
            HttpResponse("invalid")
    return render(request,"guest.html",{'key':af})
def general(request):
    pf = publicForm
    if request.method == "POST":
        pf = publicForm(request.POST, request.FILES)
        if pf.is_valid():
            pf.save()
        else:
            HttpResponse("invalid")

    return render(request,"public.html",{'key':pf})
def library(request):
    lf = libraryForm
    return render(request,"library.html",{'key':lf})


def add(request):

    k=bookForm
    if request.method == "POST":
        k = bookForm(request.POST, request.FILES)

        k.save()

    return render(request,'add.html',{'key':k})
def view_book(request):
    b=bookForm
    context = {
        'instance': b,
        'title': 'View Book'
    }
    return render(request, 'book.html', context)
