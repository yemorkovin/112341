from django.shortcuts import render, redirect
from .models import MenuItem, Users, News, Categories
from mySite.forms import Registration, Auth, AddNew

def index(request):
    context={}
    context['news'] = News.objects.all()
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def profile(request):
    us = Users.objects.all()
    print(us)
    context = {
        'uss':us
    }
    return render(request, 'profilelist.html', context=context)

def panel(request):
    user = Users.objects.filter(id__exact=request.GET.get('id'))
    context = {
        'user': user
    }
    return render(request, 'panel.html', context=context)

def save_user(request):
    user = Users()
    user.name = request.POST['name']
    user.age = request.POST['age']
    user.email = request.POST['email']
    user.poll = request.POST['poll']
    user.password = request.POST['password']
    user.save()

def reg(request):
    context = {}
    suc = 0
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            save_user(request)
            context['suc'] = 1
    else:
        form = Registration
        context['suc'] = 0
    context['form'] = form

    return render(request, 'reg.html', context=context)

def auth(request):
    context = {}
    if 'email' in request.session:
        context['email'] = request.session['email']
    if request.method == 'POST':
        form = Auth(request.POST)
        if form.is_valid():
            if Users.objects.filter(email=request.POST['email']).exists() and Users.objects.filter(password=request.POST['password']).exists():
                request.session['email'] = request.POST['email']
                return redirect('/')
    else:
        form = Auth
    context["form"] = form
    return render(request, 'auth.html', context=context)

def logout(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect('/')


def addnew(request):
    if 'email' in request.session:
        context = {}
        context['user'] = request.session['email']
        if request.method == 'POST':

            form = AddNew(request.POST)
            if form.is_valid():
                addnew = News()
                addnew.title = request.POST['title']
                addnew.text = request.POST['text']
                addnew.category = Categories.objects.filter(id=request.POST['category']).first()
                addnew.user = Users.objects.filter(email=request.session['email']).first()
                addnew.image = request.FILES['img']
                addnew.save()
        else:

            form = AddNew
        login = Users.objects.filter(email=request.session['email']).first()
        context['login'] = login
        context['form'] = form
        return render(request, 'addnew.html', context=context)
    else:
        return redirect('/')

def viewarticle(request, pk):
    context = {}
    context["new"] = News.objects.filter(id=pk).first()
    return render(request, 'articledetail.html', context=context)