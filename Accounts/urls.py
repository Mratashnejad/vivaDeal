from django.conf.urls import url
from . import views



app_name = 'accounts'

urlpatterns = [
    url(r'^login/$',views.Login_page, name='login'),
    url(r'^signup/$', views.Signup_page, name='signup'),

]