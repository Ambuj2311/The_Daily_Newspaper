from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','mob','message')

admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')

admin.site.register(category,categoryAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','passwd','ppic','address')

admin.site.register(register,registerAdmin)

class newsAdmin(admin.ModelAdmin):
    list_display = ('id','city','headlines','subject','newsdes','newspic','ndate','ncategory')

admin.site.register(news,newsAdmin)

class citiesAdmin(admin.ModelAdmin):
    list_display = ('id','cityname')
admin.site.register(cities,citiesAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display=('id','ndes','ndate')
admin.site.register(notification,notificationAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display=('id','vtitle','vdes','thumb','vlink','vdate')
admin.site.register(video,videoAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display=('id','stitle','sdes','spic','sdate')
admin.site.register(slider,sliderAdmin)

class publishadAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','company','url','advdes','banner')
admin.site.register(publishad,publishadAdmin)

class worldAdmin(admin.ModelAdmin):
    list_display = ('id','wheadlines','country','wsubject','wdes','wpic','wdate','wcategory')
admin.site.register(world,worldAdmin)










