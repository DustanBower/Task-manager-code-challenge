"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from tasks.views import TaskCreate
from tasks.views import TaskDelete
from tasks.views import TaskDetail
from tasks.views import TaskList
from tasks.views import TaskUpdate

urlpatterns = [
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^admin/', admin.site.urls),
    url(r'tasks/add/$', TaskCreate.as_view(), name='task-add'),
    url(r'tasks/(?P<pk>[0-9]+)/delete$', TaskDelete.as_view(),
        name='task-delete'),
    url(r'tasks/(?P<pk>[0-9]+)/detail$', TaskDetail.as_view(),
        name='task-detail'),
    url(r'tasks/(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-update'),
    url(r'tasks/list/$', TaskList.as_view(), name='task-list'),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index")
]
