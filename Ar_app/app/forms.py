"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm


#Under here import our models
from app.models import *

#Import parsley.js validation library
from parsley.decorators import parsleyfy

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

@parsleyfy
class CustomerForm(ModelForm):
    class Meta:
        model = customer
        exclude = ['custid']

@parsleyfy
class CustomerEditForm(ModelForm):
    class Meta:
        model = customer
        exclude = ['custid']
    #def __init__(self, custname):
    #    super (CustomerEditForm, self).__init__()
    #    if custname:
    #        self.fields['name'].queryset = customer.objects.filter(custid=customer.objects.filter(name__startswith=custname))

@parsleyfy
class JobForm(ModelForm):
    class Meta:
        model = job
        exclude = ['jobid', 'custid']

@parsleyfy
class JobEditForm(ModelForm):
    class Meta:
        model = job
        exclude = ['jobid', 'custid']

@parsleyfy
class InvForm(ModelForm):
    class Meta:
        model = invoices
        exclude = ['invoiceid', 'jobid', 'closedate', 'createdate']

@parsleyfy
class InvEditForm(ModelForm):
    class Meta:
        model = invoices
        exclude = ['invoiceid', 'jobid']

@parsleyfy
class InvEditFormSimple(ModelForm):
    class Meta:
        model = invoices
        exclude = ['invoiceid', 'jobid', 'closedate']
