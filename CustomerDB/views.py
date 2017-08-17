from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views import generic

from .models import Customer, Contract, Cluster, Version
# Create your views here.

#TODO replace with templates

def home(request):
    return render(request, 'customerDB//static/home.html')

def index(request):
    #var = "This is the CustomerDB index, login check <a href=\"cdblogin\">login</a>"
    #return HttpResponse(var)
    template = loader.get_template('customerDB/index.html')
    return HttpResponse(template.render(request))
    #return render(request, 'customerDB/index.html')


def ldapLogin(request):
    # var = "This is the LDAP login page  "
    return render(request, 'customerDB/ldaplogin.html')
    # return HttpResponse(var)


class IndexView(generic.ListView):
    template_name = 'customerDB/index.html'
    context_object_name = 'contracts_list' #This is the default value (model=Contract)
    model = Contract
    #This is the default value
    #def get_queryset(self):
    #    return Contract.objects.all()# order_by('customer')


def cust_filter(request, c_id):
    contracts_set = Contract.objects.filter(customer_id=c_id)
    return render(request, 'customerDB/index.html',{
        'contracts_list' : contracts_set,
    })

def prod_filter(request, p_id):
    contracts_set = Contract.objects.filter(product_id=p_id)
    return render(request, 'customerDB/index.html',{
        'contracts_list' : contracts_set,
    })
'''
class DetailView(generic.DetailView):
    # context_object_name = 'customer_list'
    template_name = 'customerDB/cust_detail.html'
    model = Contract'''


def DetailView(request,contr_id):
    # context_object_name = 'customer_list'
    template_name = 'customerDB/cust_detail.html'
    this_contract = Contract.objects.get(contract_id = contr_id)
    cust_name = this_contract.customer
    prod_name =  this_contract.product

    cluster_list = Cluster.objects.filter(contract = contr_id)

    return render(request, template_name, {
        'cust_name': cust_name,
        'prod_name': prod_name,
        'cluster_list': cluster_list
    })
