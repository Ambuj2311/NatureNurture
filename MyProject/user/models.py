from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=30)
    Message=models.TextField()
    def __str__(self):
        return self.Name

##############################################################

class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=500)
    sdes=models.TextField()
    spic=models.ImageField(upload_to='static/slider/',default="")
    def __str__(self):
        return self.shead
#######################################################################################
class igallery(models.Model):
    gname=models.CharField(max_length=400)
    gpic=models.ImageField(upload_to='static/gallery/',default="")
    def __str__(self):
        return self.gname
#############################################################################################

class myblog(models.Model):
    bname=models.CharField(max_length=40)
    bdes=models.TextField()
    bpic=models.ImageField(upload_to='static/blogs',null=True)
    bdate=models.DateField()
    def __str__(self):
        return self.bname

################################################################################################
class member(models.Model):
    nname=models.CharField(max_length=40)
    npincode=models.CharField(max_length=40)
    ncity=models.CharField(max_length=30)
    nemail=models.EmailField()
    nbankacount=models.CharField(max_length=60)
    ncompanyaddress=models.CharField(max_length=40)
    naddress=models.CharField(max_length=40)
    ppic=models.ImageField(upload_to='static/profile/',null=True)
    def __str__(self):
        return self.nname

class donatenow(models.Model):
    Amountvalue=models.CharField(max_length=40, null='False')
    Firstname=models.CharField(max_length=40)
    Lastname=models.CharField(max_length=40)
    Email=models.EmailField()
    Phone=models.CharField(max_length=30)
    Country=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=20)
    Occupation=models.CharField(max_length=50)
    Paypic=models.ImageField(upload_to='static/Paytm/',null=True)
    def __str__(self):
        return self.Amountvalue


class city(models.Model):
    ncity=models.CharField(max_length=30)
    cdate=models.DateField()
    def __str__(self):
        return self.ncity

class state(models.Model):
    mstate=models.CharField(max_length=30)
    mdate=models.DateField()
    def __str__(self):
        return self.mstate

class country(models.Model):
    scountry=models.CharField(max_length=40)
    sdate=models.DateField()
    def __str__(self):
        return self.scountry

class vgallery(models.Model):
    vlink=models.TextField()
    vdes=models.TextField()
    vtitle=models.CharField(max_length=200)
    vdate=models.DateField()

class event(models.Model):
    title=models.CharField(max_length=200)
    des=models.TextField()
    date=models.DateField()
    epic = models.ImageField(upload_to='static/event/', null=True)
    def __str__(self):
        return self.title




