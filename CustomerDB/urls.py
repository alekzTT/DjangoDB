from django.conf.urls import url

from . import views

app_name  = 'CustomerDB'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cust_detail/(?P<contr_id>[0-9]+)/$', views.DetailView, name='cust_detail'),
    url(r'^cust_contr/(?P<c_id>[0-9]+)/$', views.cust_filter, name='cust_contr'),
    url(r'^prod_contr/(?P<p_id>[0-9]+)/$', views.prod_filter, name='prod_contr'),
]
