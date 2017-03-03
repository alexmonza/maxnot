from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def log_in(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard:dashboard'))
    else:
        if request.method == 'POST':
            formulario = AuthenticationForm(request.POST)
            if formulario.is_valid:
                usuario = request.POST['username']
                clave = request.POST['password']
                acceso = authenticate(username=usuario, password=clave)
                if acceso is not None:
                    if acceso.is_active:
                        login(request, acceso)
                        return HttpResponseRedirect(reverse('dashboard:dashboard'))
                    else:
                        return HttpResponse("Usuario no activo")
                else:
                    dataErrorLogin = "Usuario o Password incorrectos"
                    return render(request, 'usuario/login.html',{'dataErrorLogin':dataErrorLogin})
        else:
            formulario = AuthenticationForm()

        return render(request, 'usuario/login.html')

@login_required()
def log_out(request):
    print('vamos a salir: ', request.user.username)
    logout(request)
    return HttpResponseRedirect('/')


