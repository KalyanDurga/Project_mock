from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
# Create your views here.
from app.forms import *



def home(request):
    na=request.session.get('username')
    d={'na':na}

    return render(request,'home.html',d)

def register(request):
    UFO=UserForm()
    d={'UFO':UFO}

    if request.method=='POST':
        UD=UserForm(request.POST)
        if UD.is_valid():
            UDO=UD.save(commit=False)
            password=UD.cleaned_data['password']
            UDO.set_password(password)
            UDO.save()
            
            send_mail('Registation for User',
                      'kalyan.cse.588@gmail.com',
                       'Registaion for the user form is done successfully',
                       [UDO.email],
                       fail_silently=False 
                       )
            return render(request,'submission.html')
        else:
            return HttpResponse('data is not valid')



    return render(request,'register.html',d)


def user_login(request):
    if request.method=='POST':
        un=request.POST['na']
        psw=request.POST['psw']

        AUO=authenticate(username=un,password=psw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('data is not valid')
    
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def insert_question(request):
    QFO=QuestionForm()
    d={'QFO':QFO}
    if request.method=='POST':
        un=request.session.get('username')
        na=User.objects.get(username=un)
        QD=QuestionForm(request.POST)
        if QD.is_valid():
            QDO=QD.save(commit=False)
            QDO.username=na
            QDO.save()
            return render(request,'submission.html')
        else:
            return HttpResponse('data not valid')

    return render(request,'Question_form.html',d)


class list_ques(ListView):
    model=Question
    context_object_name='que'
    template_name='Question_list.html'

@login_required
def insert_answer(request):
    d={'AO':AnswerForm()}

    if request.method=='POST':
        AD=AnswerForm(request.POST)
        if AD.is_valid():
            un=request.session.get('username')
            UD=User.objects.get(username=un)
            ADO=AD.save(commit=False)
            ADO.username=UD
            ADO.save()
            return render(request,'submission.html')
        return HttpResponse('data is not Valid')


    return render(request,'insert_answer.html',d)


class details(DetailView):
    model=Question

    context_object_name='qs'
    template_name='details.html'