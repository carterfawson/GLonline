"""
Definition of models.
"""

from django.db import models

# Create your models here.

class customer(models.Model):
    Alabama	= 'AL'
    Montana	= 'MT'
    Alaska = 'AK'
    Nebraska = 'NE'
    Arizona	= 'AZ'
    Nevada = 'NV'
    Arkansas = 'AR'
    New_Hampshire = 'NH'
    California = 'CA'
    New_Jersey = 'NJ'
    Colorado = 'CO'
    New_Mexico = 'NM'
    Connecticut = 'CT'
    New_York = 'NY'
    Delaware = 'DE'
    North_Carolina = 'NC'
    Florida = 'FL'
    North_Dakota = 'ND'
    Georgia = 'GA'
    Ohio = 'OH'
    Hawaii = 'HI'
    Oklahoma = 'OK'
    Idaho = 'ID'
    Oregon = 'OR'
    Illinois = 'IL'
    Pennsylvania = 'PA'
    Indiana = 'IN'
    Rhode_Island = 'RI'
    Iowa = 'IA'
    South_Carolina = 'SC'
    Kansas = 'KS'
    South_Dakota = 'SD'
    Kentucky = 'KY'
    Tennessee = 'TN'
    Louisiana = 'LA'
    Texas = 'TX'
    Maine = 'ME'
    Utah = 'UT'
    Maryland = 'MD'
    Vermont = 'VT'
    Massachusetts = 'MA'
    Virginia = 'VA'
    Michigan = 'MI'
    Washington = 'WA'
    Minnesota = 'MN'
    West_Virginia = 'WV'
    Mississippi = 'MS'
    Wisconsin = 'WI'
    Missouri = 'MO'
    Wyoming = 'WY'

    STATE_CHOICES = (
                 (Alabama, 'Alabama'),
                 (Alaska, 'Alaska'),
                 (Arizona, 'Arizona'),
                 (Arkansas, 'Arkansas'),
                 (California, 'California'),
                 (Colorado, 'Colorado'),
                 (Connecticut, 'Connecticut'),
                 (Delaware, 'Delaware'),
                 (Florida, 'Florida'),
                 (Georgia, 'Georgia'),
                 (Hawaii, 'Hawaii'),
                 (Idaho, 'Idaho'),
                 (Illinois, 'Illinois'),
                 (Indiana, 'Indiana'),
                 (Iowa, 'Iowa'),
                 (Kansas, 'Kansas'),
                 (Kentucky, 'Kentucky'),
                 (Louisiana, 'Louisiana'),
                 (Maine, 'Maine'),
                 (Maryland, 'Maryland'),
                 (Massachusetts, 'Massachusetts'),
                 (Michigan, 'Michigan'),
                 (Minnesota, 'Minnesota'),
                 (Mississippi, 'Mississippi'),
                 (Missouri, 'Missouri'),
                 (Montana, 'Montana'),
                 (Nebraska, 'Nebraska'),
                 (Nevada, 'Nevada'),
                 (New_Hampshire, 'New Hampshire'),
                 (New_Jersey, 'New Jersey'),
                 (New_Mexico, 'New Mexico'),
                 (New_York, 'New York'),
                 (North_Carolina, 'North Carolina'),
                 (North_Dakota, 'North Dakota'),
                 (Ohio, 'Ohio'),
                 (Oklahoma, 'Oklahoma'),
                 (Oregon, 'Oregon'),
                 (Pennsylvania, 'Pennsylvania'),
                 (Rhode_Island, 'Rhode Island'),
                 (South_Carolina, 'South Carolina'),
                 (South_Dakota, 'South Dakota'),
                 (Tennessee, 'Tennessee'),
                 (Texas, 'Texas'),
                 (Utah, 'Utah'),
                 (Vermont, 'Vermont'),
                 (Virginia, 'Virginia'),
                 (Washington, 'Washington'),
                 (West_Virginia, 'West Virginia'),
                 (Wisconsin, 'Wisconsin'),
                 (Wyoming, 'Wyoming'),
                 )
    custid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contactName = models.CharField(max_length=40)
    email = models.EmailField(max_length=245)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    #I can make it so that the States are just options from a tuple holding all the options
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class job(models.Model):
    Alabama	= 'AL'
    Montana	= 'MT'
    Alaska = 'AK'
    Nebraska = 'NE'
    Arizona	= 'AZ'
    Nevada = 'NV'
    Arkansas = 'AR'
    New_Hampshire = 'NH'
    California = 'CA'
    New_Jersey = 'NJ'
    Colorado = 'CO'
    New_Mexico = 'NM'
    Connecticut = 'CT'
    New_York = 'NY'
    Delaware = 'DE'
    North_Carolina = 'NC'
    Florida = 'FL'
    North_Dakota = 'ND'
    Georgia = 'GA'
    Ohio = 'OH'
    Hawaii = 'HI'
    Oklahoma = 'OK'
    Idaho = 'ID'
    Oregon = 'OR'
    Illinois = 'IL'
    Pennsylvania = 'PA'
    Indiana = 'IN'
    Rhode_Island = 'RI'
    Iowa = 'IA'
    South_Carolina = 'SC'
    Kansas = 'KS'
    South_Dakota = 'SD'
    Kentucky = 'KY'
    Tennessee = 'TN'
    Louisiana = 'LA'
    Texas = 'TX'
    Maine = 'ME'
    Utah = 'UT'
    Maryland = 'MD'
    Vermont = 'VT'
    Massachusetts = 'MA'
    Virginia = 'VA'
    Michigan = 'MI'
    Washington = 'WA'
    Minnesota = 'MN'
    West_Virginia = 'WV'
    Mississippi = 'MS'
    Wisconsin = 'WI'
    Missouri = 'MO'
    Wyoming = 'WY'
    
    STATE_CHOICES = (
                     (Alabama, 'Alabama'),
                     (Alaska, 'Alaska'),
                     (Arizona, 'Arizona'),
                     (Arkansas, 'Arkansas'),
                     (California, 'California'),
                     (Colorado, 'Colorado'),
                     (Connecticut, 'Connecticut'),
                     (Delaware, 'Delaware'),
                     (Florida, 'Florida'),
                     (Georgia, 'Georgia'),
                     (Hawaii, 'Hawaii'),
                     (Idaho, 'Idaho'),
                     (Illinois, 'Illinois'),
                     (Indiana, 'Indiana'),
                     (Iowa, 'Iowa'),
                     (Kansas, 'Kansas'),
                     (Kentucky, 'Kentucky'),
                     (Louisiana, 'Louisiana'),
                     (Maine, 'Maine'),
                     (Maryland, 'Maryland'),
                     (Massachusetts, 'Massachusetts'),
                     (Michigan, 'Michigan'),
                     (Minnesota, 'Minnesota'),
                     (Mississippi, 'Mississippi'),
                     (Missouri, 'Missouri'),
                     (Montana, 'Montana'),
                     (Nebraska, 'Nebraska'),
                     (Nevada, 'Nevada'),
                     (New_Hampshire, 'New Hampshire'),
                     (New_Jersey, 'New Jersey'),
                     (New_Mexico, 'New Mexico'),
                     (New_York, 'New York'),
                     (North_Carolina, 'North Carolina'),
                     (North_Dakota, 'North Dakota'),
                     (Ohio, 'Ohio'),
                     (Oklahoma, 'Oklahoma'),
                     (Oregon, 'Oregon'),
                     (Pennsylvania, 'Pennsylvania'),
                     (Rhode_Island, 'Rhode Island'),
                     (South_Carolina, 'South Carolina'),
                     (South_Dakota, 'South Dakota'),
                     (Tennessee, 'Tennessee'),
                     (Texas, 'Texas'),
                     (Utah, 'Utah'),
                     (Vermont, 'Vermont'),
                     (Virginia, 'Virginia'),
                     (Washington, 'Washington'),
                     (West_Virginia, 'West Virginia'),
                     (Wisconsin, 'Wisconsin'),
                     (Wyoming, 'Wyoming'),
                     )
    jobid = models.AutoField(primary_key=True)
    custid = models.ForeignKey('customer')
    description = models.TextField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    #I can make it so that the States are just options from a tuple holding all the options
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return self.custid.name

#class estimate(models.Model):
#    import datetime
#    estimateid = models.AutoField(primary_key=True)
#    jobid = models.ForeignKey(job)
#    estclass = models.CharField(max_length = 20)
#    description = models.TextField()
#    createdate = models.DateTimeField(default=datetime.datetime.now())
#    closedate = models.DateTimeField(null=True)
#    payapp_num = models.IntegerField()
#    active = models.BooleanField(default=True)

class invoices(models.Model):
    import datetime
    invoiceid = models.AutoField(primary_key=True)
    jobid = models.ForeignKey('job')
    description = models.TextField()
    createdate = models.DateField(default=datetime.datetime.now().date())
    closedate = models.DateField(null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.jobid.name

#class est_lineitems(models.Model):
#    lineID = models.AutoField(primary_key=True)
#    estid = models.ForeignKey('estimate')
#    description = models.TextField()
#    account = models.CharField(max_length=20)
#    amount = models.FloatField()

class inv_lineitems(models.Model):
    lineID = models.AutoField(primary_key=True)
    #estid = models.ForeignKey('estimate')
    invid = models.ForeignKey('invoices', null=True)
    #estliid = models.ForeignKey('est_lineitems', null=True)
    description = models.TextField()
    account = models.CharField(max_length=20)
    amount = models.FloatField()

class payment(models.Model):
    import datetime
    payid = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.datetime.now())

class payment_lineitem(models.Model):
    pay_li_id = models.AutoField(primary_key=True)
    lineID = models.ForeignKey('inv_lineitems')
    payid = models.ForeignKey('payment')
    #Should I put the amount on here because there could be partial payments on a particular line item?
    #I could also just put the amount in the payment class...
    amount = models.FloatField()


#class account_codes(models.Model):
#    account_cd = models.CharField(max_length=30, primary_key=True)
#    account_descr = models.CharField(max_length=30)
#    account_dbtpos = models.BooleanField()

#class transactions(models.Model):
#    import datetime
#    transaction_cd = models.AutoField(primary_key=True)
#    #This means that a transaction must be connected to an invoice
#    invoiceid = models.ForeignKey('invoices')
#    datetime = models.DateTimeField(default=datetime.datetime.now()))

#class debits(models.Model):
#    debit_cd = models.AutoField(primary_key=True)
#    account_cd = models.ForeignKey('account_codes')
#    transaction_cd = models.ForeignKey('transactions')
#    amount = models.FloatField()

#class credits(models.Model):
#    credit_cd = models.AutoField(primary_key=True)
#    account_cd = models.ForeignKey('account_codes')
#    transaction_cd = models.ForeignKey('transactions')
#    amount = models.FloatField()






