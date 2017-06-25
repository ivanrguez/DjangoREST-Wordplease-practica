from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View


from tasks.form import PostForm
from tasks.models import Post, Categorias


def post_list(request):

    # recupera todas las tareas
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