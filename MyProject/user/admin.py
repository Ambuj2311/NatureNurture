from django.contrib import admin
from .models import  *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Mobile","Message")

admin.site.register(contactus,contactusAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic')

admin.site.register(igallery,igalleryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic')

admin.site.register(slider,sliderAdmin)

class myblogAdmin(admin.ModelAdmin):
    list_display = ('id','bname','bdes','bpic','bdate')

admin.site.register(myblog,myblogAdmin)

class memberAdmin(admin.ModelAdmin):
    list_display = ('id','nname','npincode','ncity','nemail','nbankacount','ncompanyaddress','naddress','ppic')
admin.site.register(member,memberAdmin)


class donatenowAdmin(admin.ModelAdmin):
    list_display = ('id','Amountvalue','Firstname','Lastname','Email','Phone','Country','Address','State','Pincode','Occupation','Paypic')

admin.site.register(donatenow,donatenowAdmin)


class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','cdate')

admin.site.register(city,cityAdmin)

class stateAdmin(admin.ModelAdmin):
    list_display = ('id','mstate','mdate')

admin.site.register(state,stateAdmin)

class countryAdmin(admin.ModelAdmin):
    list_display = ('id','scountry','sdate')

admin.site.register(country,countryAdmin)

class vgalleryAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vdes','vtitle','vdate')

admin.site.register(vgallery,vgalleryAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','title','des','date','epic')

admin.site.register(event,eventAdmin)