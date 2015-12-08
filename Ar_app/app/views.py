"""
Definition of views.
"""

from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from datetime import datetime
from app.forms import *
from app.models import *
from django.core.urlresolvers import reverse


"""This view renders the home page."""

def home(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        'app/index.html',
        context
    )

"""This view renders the customers page."""
def customers(request):
    assert isinstance(request, HttpRequest)
    customer_list = customer.objects.all()

    if request.method == 'POST':
        cusForm = CustomerForm(request.POST)
        if cusForm.is_valid():
            cusForm.save()
            return HttpResponseRedirect('/customers')
    else:
        cusForm = CustomerForm() 

    context = RequestContext(request, {
        'customers':customer_list,
        'cus_form':cusForm
        })
    return render(
        request,
        'app/customers.html',
        context
    )

"""This view renders the jobs for a specific customer page."""
def customer_specific(request, custid_url):
    assert isinstance(request, HttpRequest)

    job_list = job.objects.filter(custid=customer.objects.get(custid=custid_url))
    custurl = '/customer/' + str(custid_url) + '/'
    cust = customer.objects.get(custid=custid_url)
    
    if request.method == 'POST':
        if 'edit_customer' in request.POST:
        #This is where I put the edit form response
            cusFormEdit = CustomerEditForm(request.POST)
            if cusFormEdit.is_valid():
                #here is where I grab the cleaned_data from the form and then use it to alter the current model instance.
                cust.name = cusFormEdit.cleaned_data['name']
                cust.contactName = cusFormEdit.cleaned_data['contactName']
                cust.email = cusFormEdit.cleaned_data['email']
                cust.address = cusFormEdit.cleaned_data['address']
                cust.city = cusFormEdit.cleaned_data['city']
                cust.state = cusFormEdit.cleaned_data['state']
                cust.zip = cusFormEdit.cleaned_data['zip']
                cust.phone = cusFormEdit.cleaned_data['phone']
                cust.save()
            return HttpResponseRedirect(custurl)
        elif 'new_job' in request.POST:
        #This is where I put the new job form response
            jobForm = JobForm(request.POST)
            if jobForm.is_valid():
                newjob = job(custid=cust, description=jobForm.cleaned_data['description'], address=jobForm.cleaned_data['address'], city=jobForm.cleaned_data['city'], state=jobForm.cleaned_data['state'], zip=jobForm.cleaned_data['zip'])
                newjob.save()
            return HttpResponseRedirect(custurl)
        else:
            print(security)
    else:
        jobForm = JobForm()
        cusFormEdit = CustomerEditForm(instance=customer.objects.get(custid=custid_url))

    context = RequestContext(request, {
                             'jobs':job_list,
                             'job_form':jobForm,
                             'cus_form_edit':cusFormEdit,
                             'cust':cust,
                             })
    return render(
              request,
              'app/jobs.html',
              context
              )

"""This view renders the invoices for a specific job."""
def job_specific(request, custid_url, jobid_url):
    assert isinstance(request, HttpRequest)

    custurl = '/job/' + str(custid_url) + '/' + str(jobid_url) + '/'
    joblist = job.objects.filter(custid=customer.objects.get(custid=custid_url))
    job_spec = job.objects.get(jobid=jobid_url)
    cust = customer.objects.get(custid=custid_url)
    inv_list = invoices.objects.filter(jobid=jobid_url)


    if request.method == 'POST':
        if 'edit_job' in request.POST:
#This is where I put the edit form response
            jobFormEdit = JobEditForm(request.POST)
            if jobFormEdit.is_valid():
        #here is where I grab the cleaned_data from the form and then use it to alter the current model instance.
                job_spec.description = jobFormEdit.cleaned_data['description']
                job_spec.address = jobFormEdit.cleaned_data['address']
                job_spec.state = jobFormEdit.cleaned_data['state']
                job_spec.zip = jobFormEdit.cleaned_data['zip']
                job_spec.save()
            return HttpResponseRedirect(custurl)
        elif 'new_invoice' in request.POST:
            #This is where I put the new job form response
            invForm = InvForm(request.POST)
            if invForm.is_valid():
                datetime.now().date()
                newinv = invoices(jobid=job_spec, description=invForm.cleaned_data['description'], active=invForm.cleaned_data['active'], amount=invForm.cleaned_data['amount'])
                newinv.save()
            return HttpResponseRedirect(custurl)
        else:
            print('security')
    else:
        jobFormEdit = JobEditForm(instance=job.objects.get(jobid=jobid_url))
        invForm = InvForm()

    context = RequestContext(request, {
                             'invs':inv_list,
                             'inv_form':invForm,
                             'job_spec':job_spec,
                             'job_form_edit':jobFormEdit,
                             'cust':cust
                             })
    return render(
              request,
              'app/invoices.html',
              context
              )

def inv_specific(request, jobid_url, invid_url):
    assert isinstance(request, HttpRequest)
    inv_spec = invoices.objects.get(invoiceid=invid_url)
    cust_url = '/invoice/' + str(jobid_url) + '/' + str(invid_url) + '/'
    flag = 1
    
    if request.method == 'POST':
        if 'edit_invoice' in request.POST:
            invformedit = InvEditForm(request.POST)
            if invformedit.is_valid():
                inv_spec.description = invformedit.cleaned_data['description']
                inv_spec.amount = invformedit.cleaned_data['amount']
                inv_spec.createdate = invformedit.cleaned_data['createdate']
                if inv_spec.active == True:
                    if invformedit.cleaned_data['active'] == False:
                        inv_spec.closedate = datetime.now().date()
                inv_spec.active = invformedit.cleaned_data['active']
                inv_spec.save()
            return HttpResponseRedirect(cust_url)
        elif 'edit_invoice_simple' in request.POST:
            invformedit = InvEditFormSimple(request.POST)
            if invformedit.is_valid():
                inv_spec.description = invformedit.cleaned_data['description']
                inv_spec.amount = invformedit.cleaned_data['amount']
                inv_spec.createdate = invformedit.cleaned_data['createdate']
                if inv_spec.active == True:
                    if invformedit.cleaned_data['active'] == False:
                        inv_spec.closedate = datetime.now().date()
                inv_spec.active = invformedit.cleaned_data['active']
                inv_spec.save()
            return HttpResponseRedirect(cust_url)
        else:
            print('security')

    else:
        invformedit = InvEditForm(instance=invoices.objects.get(invoiceid=invid_url))
        invformeditsimple = InvEditFormSimple(instance=invoices.objects.get(invoiceid=invid_url))
    if inv_spec.active == False:
        context = RequestContext(request, {
                             'inv_spec':inv_spec,
                             'invformedit':invformedit,
                             'invformeditsimple':invformeditsimple,
                             'flag':flag
                             })
    else:
        context = RequestContext(request, {
                                 'inv_spec':inv_spec,
                                 'invformedit':invformedit,
                                 'invformeditsimple':invformeditsimple
                                 })
    return render(
                  request,
                  'app/invoice-detail.html',
                  context
                  )