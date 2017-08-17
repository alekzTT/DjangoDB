from django.db import models
from django.db.models.fields import AutoField
from _overlapped import NULL

from .forms import NameForm
# Create your models here.

class Roles(models.Model):
    role_id = models.AutoField(primary_key = True)
    
    role_name = models.CharField(max_length = 15, unique = True)
    role_description = models.CharField(max_length = 200, default = 'contact role')
    
    def __str__(self):
        return str(self.role_description)
    
    
class Customer(models.Model):
    
    customer_id = models.AutoField(primary_key = True)
    customer_name = models.CharField(max_length = 200, unique = True)
    ras_procedure = models.FileField(null = True, blank=True)
    
    
    def __str__(self):
        
        #return self.customer_name
        return str(self.customer_name)
    
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    
    product_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_name
    
  
class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.contract_id)
    
    
class ContactInfo(models.Model):
    contact_id = models.AutoField(primary_key = True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    role = models.ForeignKey(Roles, on_delete = models.CASCADE)
    contact_person = models.CharField(max_length = 200)
    contact_email = models.EmailField
    contact_phone = models.CharField(max_length = 15)
    contact_mobile = models.CharField(max_length = 15)
    form = NameForm()
    def __str__(self):
        return self.contact_person
    
    
class Version(models.Model):
    version_id = models.AutoField(primary_key = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    version_name = models.CharField(max_length = 20)    
    
    def __str__(self):
        return self.version_name
    
class Cluster(models.Model):
    cluster_id = models.AutoField(primary_key = True)
    contract = models.ForeignKey(Contract, on_delete = models.CASCADE)
    version = models.ForeignKey(Version, on_delete = models.CASCADE)
    
    cluster_name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.cluster_name


class Third_party(models.Model):
    company_id = models.AutoField(primary_key = True)
    
    ticket_link = models.URLField(null = True)
    company_name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.company_name
    


class HardWare(models.Model):
    model_id = models.AutoField(primary_key = True)
    company = models.ForeignKey(Third_party, on_delete = models.CASCADE)

    model_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.model_name
    
    
class Node(models.Model):
    node_id = AutoField(primary_key = True)
    hw_models = models.ForeignKey(HardWare, on_delete = models.CASCADE)
    
    node_name = models.CharField(max_length = 30)
    node_ip = models.IPAddressField
    
    def __str__(self):
        return self.node_name
    


    

    

    
    
            
    
    
    
    
    
    
    
    
