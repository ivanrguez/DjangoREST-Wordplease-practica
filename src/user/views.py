from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from tasks.registro import RegistroForm
from user.forms import LoginForm


class LoginView(View):

    def get(selft, request):

        context = {
        'form': LoginForm()
        }

        return render(request, 'login.html', context)

    def post(selft, request):
        form = LoginForm(request.POST)
        context = dict()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                #usuario autenticado
                django_login(request,user)
                url = request.GET.get('next', 'new_post')
                return  redirect(url)
            else:
                #usuario no autenticado
                context['error'] = 'error username o password'
            context['form'] = form
        return render(request, 'login.html', context)

def logout(request):
    django_logout(request)
    return redirect('login')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'tasks/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('new_post')
