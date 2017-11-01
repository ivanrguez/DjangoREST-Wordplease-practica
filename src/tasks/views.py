from datetime import date

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View


from tasks.form import PostForm, CommentForm
from tasks.models import Post, Categorias

def home(request):

    # recupera todas las tareas
    post = Post.objects.order_by('-created_at').all()




    #crea la representacion de los datos
    context ={
        'post_objects': post,

    }

    #responder
    return render(request, 'tasks/home.html', context)

def post_list(request):

    # recupera todas las tareas
    #publico = Post.Estado.objects.get(estado='publico')
    if not request.user.is_authenticated:
        post = Post.objects.filter(estado='PUB').order_by('-created_at')

    else:
        post = Post.objects.order_by('-created_at').all()



    #crea la representacion de los datos
    context ={
        'post_objects': post,

    }

    #responder
    return render(request, 'tasks/blogs.html', context)

@login_required()
def mis_post(request, user):

    # recupera todas las tareas
    try:
        u = User.objects.get(username=user).id
        post = Post.objects.filter(user=u).order_by('-created_at')
    except Post.DoesNotExist:
        return render(request, '404.html', {}, status=404)
    except Post.MultipleObjectsReturned:
        return HttpResponse('existen varias tareas con ese identificador', status=300)


    #crea la representacion de los datos
    context ={
        'mi_post': post
    }

    #responder
    return render(request, 'tasks/mi_post.html', context)

@login_required()
def post_detalle(request, user, post_pk):

    try:
        u = User.objects.get(username=user).id
        post = Post.objects.filter(user=u).select_related().get(pk=post_pk)

    except Post.DoesNotExist:
        return render(request, '404.html', {}, status=404)
    except Post.MultipleObjectsReturned:
        return HttpResponse('existen varias tareas con ese identificador', status=300)
    context = {
        'post': post
    }
    return render(request, 'tasks/detalle.html', context)


class NewPost(View):

    def get(self, request):
        form = PostForm()

        context = {
            'form': form
        }
        return render(request, 'tasks/new.html', context)


    def post(self, request):

        post_user = Post(user=request.user)
        form =PostForm(request.POST, instance=post_user)

        if form.is_valid():

            new = form.save()

            mensaje = 'tarea creada '
            form = PostForm()
        else:
            mensaje ='se ha producido un  error'

        context = {

            'form': form,
            'mensaje':mensaje
        }

        return render(request, 'tasks/new.html', context)


class View(View):
    def add_comment_to_post(request, user, post_pk):
        post = render(request, '404.html', {}, status=404)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save()
                comment.post =  post
                comment.save()
                return redirect('detalle', user, pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'tasks/add_comment_to_post.html', {'form': form})
