from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = slider.objects.all().order_by('-id')[0:2]
    bdata=myblog.objects.all().order_by('-id')[0:3]
    im=igallery.objects.all().order_by('-id')
    card=event.objects.all().order_by('-id')[0:4]
    mydict={"res":data,'data':bdata,'img':im,'evt':card}
    return render(request, 'user/index.html',context=mydict)
################################################
def about(request):
    return render(request,'user/about.html')
#################################################

def contact(request):
    Status = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mob')
        message = request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        Status = True
    return render(request, 'user/contact.html',context={"msg":Status})
######################################################
def video(request):
    data=vgallery.objects.all().order_by('-id')
    myd={"vdata":data}

    return render(request,'user/video.html',myd)
######################################################
def gallery(request):
    d=igallery.objects.all().order_by('-id')
    mydict={"data":d}
    return render(request,'user/gallery.html',context=mydict)
######################################################

def blog(request):
    bdata=myblog.objects.all().order_by('-id')
    if request.method=="POST":
        s=request.POST.get('search')
        if s is not "":
           bdata=myblog.objects.all().filter(Q(bname__icontains=s)|Q(bdes__icontains=s))
        else:
            return HttpResponse("<script>alert('Please Enter Data For Search');location.href='/user/blog/'</script>")
    mydict={"bdata":bdata}
    return render(request,'user/blog.html',context=mydict)
######################################################
def membership(request):
    Status = False
    cities=city.objects.all().order_by('-id')
    if request.method == "POST":
        name = request.POST.get('name')
        pincode = request.POST.get('pincode')
        c=request.POST.get('city')
        email=request.POST.get('email')
        bankaccount=request.POST.get('bankaccount')
        companyaddress=request.POST.get('companyaddress')
        address=request.POST.get('address')
        pic=request.FILES.get('ppic')
        member(nname=name,npincode=pincode,ncity=c,nemail=email,nbankacount=bankaccount,ncompanyaddress=companyaddress,naddress=address,ppic=pic).save()
        Status = True
    return render(request,'user/membership.html',context={"ct":cities,"mng":Status})
######################################################
def donate(request):
    Status = False
    con=country.objects.all().order_by('-id')
    statey=state.objects.all().order_by('-id')
    if request.method == "POST":
        amountvalue=request.POST.get('amountvalue')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        c=request.POST.get('country')
        address=request.POST.get('address')
        s=request.POST.get('state')
        pincode=request.POST.get('pincode')
        occupation=request.POST.get('occupation')
        paypic=request.FILES.get('ppic')
        donatenow(Amountvalue=amountvalue,Firstname=firstname,Lastname=lastname,Email=email,Phone=phone,Country=c,Address=address,State=s,Pincode=pincode,Occupation=occupation,Paypic=paypic).save()
        Status = True
    return render(request,'user/donate.html',context={"st":statey,"cct":con,"nsg":Status})
#######################################################
def causes(request):
    return render(request, 'user/causes.html')

def vdodetails(request):
    y=request.GET.get('msg')
    x=vgallery.objects.all().filter(id=y)
    myd={"vdata":x}
    return render(request,'user/details.html',myd)

def evdetails(request):
    p=request.GET.get('psg')
    b=event.objects.all().filter(id=p)
    mydect={"evt":b}
    return render(request,'user/eventdetails.html',mydect)

def blogdetail(request):
    a=request.GET.get('bsg')
    d=myblog.objects.all().filter(id=a)
    md={"data":d}
    return render(request,'user/Blogdetails.html',md)


def sldetails(request):
    s=request.GET.get('ssg')
    l=slider.objects.all().filter(id=s)
    myd={"res":l}
    return render(request,'user/sliderdetails.html',myd)


def myprofile(request):
    return render(request,'user/myprofile.html')

def login(request):
    return render(request,'user/login.html')


