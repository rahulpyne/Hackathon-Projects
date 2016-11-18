from django.conf.urls import url,include
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^signup', views.signup, name='signup'),
url(r'^login', views.login, name='login'),
url(r'^meal_plan', views.initialInfo, name='meal_plan'),
url(r'^initial-info', views.initialInfo, name='initial-info')]
