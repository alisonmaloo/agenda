from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages

def login(request):
    return render (request,'login_html')

def logout(request):
    logout (request)
    return redirect ('/')

 def submir(request):
    if request.POST:
        username=request.POST.get('username')
        passworld=request.POST.get('passworld')
        usuario=authenticate(username=username,passworld=passworld)
        if usuario is not None:
            login(request=usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuario ou senha invalidos")
    
    return redirect('/')


@login_required(login_url='login/') 
def index (request):
    return redirect('/agenda/')
def lista_eventos(request):
    usuario=request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = ('eventos', evento)
    return render(request, 'agenda.html', dados)


