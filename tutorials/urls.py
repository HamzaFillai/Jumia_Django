from django.urls import re_path
from tutorials import views

urlpatterns = [
	  re_path(r'^api/users$', views.tutorial_list),
	  re_path(r'^api/users/(?P<pk>[0-9]+)$', views.tutorial_detail),
	  re_path(r'^api/login$', views.login),
	  re_path(r'^api/cluster$', views.clickstream),
	  re_path(r'^api/recommandation', views.recommand),
]