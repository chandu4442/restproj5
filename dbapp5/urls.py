from django.conf.urls import url
from . import views
app_name='dbapp'
urlpatterns = [
url(r'^$',views.input, name='input'),

url(r'^display$',views.display,name='display'),
url(r'^products/$', views.ProductList.as_view()),
]