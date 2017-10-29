"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from tasks.api import TaskViewSet, BlogsViewSet
from tasks.views import post_list, post_detalle, mis_post, NewPost, home
from user.api import UserViewSet

from user.views import LoginView, logout, RegistroUsuario

router = DefaultRouter()
router.register("user", UserViewSet, base_name="user_api")
router.register("tasks", TaskViewSet)
router.register("blogs", BlogsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^blogs$', post_list, name='post_list'),
    url(r'^signup$', RegistroUsuario.as_view(), name='RegistroUsuario'),
    url(r'^blogs/(?P<user>[-\w]+)/$', mis_post, name='mis_post'),
    url(r'^new-post$', NewPost.as_view(), name='new_post'),
    url(r'^blogs/(?P<user>[-\w]+)/(?P<post_pk>[0-9]+)$', post_detalle, name='post_detalle'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', logout, name='logout'),

# API Users & Tasks
    url(r'^api/1.0/', include(router.urls)),



]
