"""maasin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from post import views as post_views

urlpatterns = [
    path('admin/',                          admin.site.urls),
    path('',                                users_views.index,                  name='index'),
    path('login/',                          post_views.login_form,              name='login'),
    path('news/view/<int:id>/',             users_views.view,                   name='view'),
    path('news/view/more/',                 users_views.view_more,              name='view_more'),
    path('academics/',                      users_views.academics,              name='academics'),
    path('alma-matter-song/',               users_views.song,                   name='song'),
    path('code-of-conduct/',                users_views.codeofconduct,          name='codeofconduct'),
    path('admission-and-policies/',         users_views.admission,              name='admission'),
    path('founder/',                        users_views.founder,                name='founder'),
    path('scholarship/',                    users_views.scholarship,            name='scholarship'),
    path('bsit-homepage/',                  users_views.bsit_homepage,          name='bsit_homepage'),
    path('bsn-homepage/',                   users_views.bsn_homepage,           name='bsn_homepage'),
    path('bsa-homepage/',                   users_views.bsa_homepage,           name='bsa_homepage'),
    path('laed-homepage/',                  users_views.laed_homepage,          name='laed_homepage'),
    path('fpst-homepage/',                  users_views.fpst_homepage,          name='fpst_homepage'),
    path('bsa-homepage/',                   users_views.bsa_homepage,           name='bsa_homepage'),
    path('bsba-homepage/',                  users_views.bsba_homepage,          name='bsba_homepage'),
####################    FOR ADMIN LOG IN, POST, LOG OUT ROUTES    ################################
    path('admin/post/list/',                post_views.post_list,               name='post_list'),
    path('admin/post/ist/add/',             post_views.add_post,                name='add_post'),
    path('admin/post/update/<int:id>/',     post_views.update_post,             name='update_post'),
    path('admin/post/delete/<int:id>/',     post_views.delete_post,             name='delete_post'),
]

