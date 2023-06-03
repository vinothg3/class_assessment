from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from app.form import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,DetailView


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d1={'username':username}
        return render(request,'app/home.html',d1)
    return render(request,'app/home.html')

def registerform(request):
    rf=user_form()
    d={'rf':rf}
    if request.method=='POST':
        uf=user_form(request.POST)
        rp=request.POST['rp']
        
        
        if uf.is_valid():
            p=uf.cleaned_data['password']
            if p==rp:
                UFD=uf.save(commit=False)
                UFD.set_password(uf.cleaned_data['password'])
                UFD.save()
                send_mail('registerform','your register successfully','kerukkucreation@gmail.com',[UFD.email],fail_silently=True)
                return HttpResponse('successfully')
            else:
                return HttpResponse('passwword not valid')
            
        else:
            return HttpResponse(' not valid ')
    return render(request,'app/registerform.html',d)



def userlog(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        ATC=authenticate(username=username,password=password)
        print('hi')
        if ATC and ATC.is_active:
            login(request,ATC)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('not valid')
    return render (request,'app/userlog.html')

@login_required
def userout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def questions(request):
    qs=question_form()
    ql=Question.objects.all()
    al=Allanswer.objects.all()
    d={'qs':qs,'ql':ql,'al':al}
    if request.method=='POST':
        qus=question_form(request.POST)
        username=request.session.get('username')
        print(username)
        ku=User.objects.get(username=username)
        if qus.is_valid():
            k=qus.save(commit=False)
            k.username=ku
            k.save()
        return HttpResponseRedirect(reverse('Questionlist'))
    return render(request,'app/questions.html',d)

@login_required
def answers(request):
    aw=answer_form()
    anl=Allanswer.objects.all()
    d={'aw':aw,'anl':anl}
    if request.method=='POST':
        qus=answer_form(request.POST)
        username=request.session.get('username')
        print(username)
        ku=User.objects.get(username=username)
        if qus.is_valid():
            un=qus.save(commit=False)
            un.username=ku
            un.save()
        return HttpResponseRedirect(reverse('Questionlist'))
    return render(request,'app/answers.html',d)

class Questionlist(ListView):
    model=Question
    fields=['username','question']
    context_object_name='li'

class Questiondetail(DetailView):
    model=Question
    context_object_name='qu'