from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.main, name='main'),
    url(r'^country_base', views.country_base, name='posts'),
    url(r'^disease_base', views.disease_base, name='posts'),
    url(r'^disease2_base', views.disease2_base, name='posts'),
    url(r'^discover_base', views.discover_base, name='posts'),
    url(r'^Users_base', views.Users_base, name='posts'),
    url(r'^Publicservant_base', views.Publicservant_base, name='posts'),
url(r'^Doctor_base', views.Doctor_base, name='posts'),
url(r'^Specialize_base', views.Specialize_base, name='posts'),
url(r'^Record_base', views.Record_base, name='posts'),
url(r'^q1', views.q1, name='posts'),
url(r'^q2', views.q2, name='posts'),
url(r'^q3', views.q3, name='posts'),
url(r'^q4', views.q4, name='posts'),
url(r'^q5', views.q5, name='posts'),

path('work/new/', views.C_, name='C_'),
path('work/new2/', views.DT_, name='DT_'),
path('work/new3/', views.Dise_, name='Dise_'),
path('work/new4/', views.Disc_, name='Disc_'),
path('work/new5/', views.Doc_, name='Doc_'),
path('work/new6/', views.P_, name='P_'),
path('work/new7/', views.U_, name='U_'),
path('work/new8/', views.R_, name='R_'),
path('work/new9/', views.S_, name='S_'),


]