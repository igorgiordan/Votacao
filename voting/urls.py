from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as voting

app_name = 'voting'

urlpatterns = [

    path('', voting.Index.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/novo/', voting.UserCreateView.as_view(), name='user-create'),
    path('criarproposta/', voting.AddProposalView.as_view(), name='proposal-create'),
    path('vote/<pk>', voting.Vote.as_view(), name='vote'),
    path('votosim/', voting.Approve.as_view(), name='votosim'),
    path('comentar/', voting.CommentView.as_view(), name='comentar'),
    path('comentarios/<pk>/', voting.Vote2.as_view(), name='comentarios'),
]