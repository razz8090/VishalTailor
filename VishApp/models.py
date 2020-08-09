from django.db import models




class Administator(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Cust_info(models.Model):
    invoice = models.IntegerField( blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    shirt = models.IntegerField()
    pant = models.IntegerField()
    Total_amount = models.IntegerField( null=False, blank=False)
    rem_amount = models.IntegerField( blank=False)
    recived_amount = models.IntegerField(null=True, blank=True)
    delevery_date = models.DateField(auto_now=False)
    oder_date = models.DateField(auto_now=False)
    status = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Shirt_de(models.Model):
    invoice_s = models.IntegerField(primary_key=True)
    name_s = models.CharField(max_length=100)
    sl = models.IntegerField()
    sm1 = models.IntegerField()
    ss = models.IntegerField()
    sb = models.IntegerField()
    sm2 = models.IntegerField()
    s_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name_s

class Pant_de(models.Model):
    invoice_p = models.IntegerField(primary_key=True )
    name_p = models.CharField(max_length=100)
    pl = models.IntegerField()
    p_k = models.IntegerField()
    ph1 = models.IntegerField()
    pg = models.IntegerField()
    ph2 = models.IntegerField()
    p_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name_p

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)
    adress = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    pin = models.IntegerField(null= False)
    phone = models.IntegerField(null=False)
    email = models.EmailField()
    adhar = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Emp_Record(models.Model):
    emp_id = models.IntegerField(null=False,blank=False)
    date = models.DateField(primary_key=True)
    pant = models.IntegerField()
    shirt = models.IntegerField()
    stepend = models.IntegerField()

    def __int__(self):
        return self.emp_id
