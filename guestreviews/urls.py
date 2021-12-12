from django.urls import path
from .import views
urlpatterns=[path('', views.home,name='home'),
             path('admini', views.admini,name='admini'),
             path('guest', views.guest,name='guest'),
             path('general', views.general,name='general'),
             path('library', views.library,name='library'),
             path('add', views.add,name='add'),
             ]