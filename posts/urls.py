from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^post_list', views.PostList.as_view(), name="post_list"), #expresiones regulares 
	url(r'^nuevo/$', views.NuevoPost.as_view(), name="nuevo"),
	url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detail"), #Para el detalle de cada uno de los posts
	#el signo $ es para decirle que no va a recibir nada.
]