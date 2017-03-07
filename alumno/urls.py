from django.conf.urls import url
from .views import AlumnoList, AlumnoCreate, AlumnoDetail

urlpatterns = [
    url(r'^$', AlumnoList.as_view() ,name='lista-alumnos'),
    url(r'^(?P<pk>[0-9]+)/$', AlumnoDetail.as_view(), name='alumno-detail'),
    url(r'add/$', AlumnoCreate.as_view(success_url="/alumnos/") ,name='alumno-add'),
]