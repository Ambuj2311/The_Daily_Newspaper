from django.http import HttpResponse
from django.shortcuts import render
from .models import * #contact,category
# Create your views here.
def home(request):
    cdata=category.objects.all().order_by('-id')[0:6] #order by -id means descending order of id
    ndata=news.objects.all().order_by('-id')[0:12]
    ncity = cities.objects.all().order_by('-id')
    data=notification.objects.all().order_by('-id')[0:4]
    sdata=slider.objects.all().order_by('-id')[0:4]
    wdata=world.objects.all().order_by('-id')[0:6]
    return render(request,'thedailynewspaper/index.html',{"data":cdata,"news":ndata,"citys:":ncity,"notification":data,"slider":sdata,"world":wdata})

def about(request):
    return render(request,'thedailynewspaper/about.html')

def contactus(request):
    status=False
    if request.method=='POST':
        #mydict={"A":"AMBUJ","B":"CSJM","C":"7390923288"}
        Name=request.POST.get("name","") #second quote is used to give default value to the variable
        Email=request.POST.get("email","") #second quote is used to give default value to the variable
        Mobile=request.POST.get("mobile","") #second quote is used to give default value to the variable
        Message=request.POST.get("msg","") #second quote is used to give default value to the variable
        x=contact(name=Name,email=Email,mob=Mobile,message=Message)   #contact is the table name/class name
        x.save()
        status=True

    return render(request,'thedailynewspaper/contactus.html',{'S':status})

def videos(request):
    vdata=video.objects.all().order_by('-id')
    return render(request,'thedailynewspaper/videos.html',{'video':vdata})

def viewnews(request):
    cdata=category.objects.all().order_by('id')
    a = request.GET.get('abc')
    ndata=""
    if a is None:
        ndata = news.objects.all().order_by('-id')
    else:
        ndata=news.objects.filter(ncategory=a).order_by('-id')
    return render(request,'thedailynewspaper/viewnews.html/',{"c":cdata,"n":ndata})


def profile(name, mobile, email, passwd, address, fu):
    pass


def register(request):
    if request.method=='POST':
        Name=request.POST.get("name","")
        Mobile=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Password=request.POST.get("passwd","")
        Address=request.POST.get("address","")
        picname=request.FILES["fu"]
        register(name=Name,mobile=Mobile,email=Email,passwd=Password,address=Address,fu=picname).save()
        return HttpResponse("<script> alert ('You are successfully  registered...');window.location.href='/thedailynewspaper/resister/'</script>")
    return render(request,'thedailynewspaper/registration.html')

def viewmore(request):
    a=request.GET.get('msg')
    ndata=news.objects.filter(id=a)
    b=request.GET.get('abc')
    wdata=world.objects.filter(id=b)
    return render(request, 'thedailynewspaper/viewmore.html', {"data":ndata,"w":wdata})


def publish(request):
    status = False
    if request.method == 'POST':
        # mydict={"A":"AMBUJ","B":"CSJM","C":"7390923288"}
        Name = request.POST.get("name", "")  # second quote is used to give default value to the variable
        Email = request.POST.get("email", "")  # second quote is used to give default value to the variable
        Mobile = request.POST.get("mobile", "")  # second quote is used to give default value to the variable
        Cname = request.POST.get("cname", "")  # second quote is used to give default value to the variable
        Url = request.POST.get("webad", "")  # second quote is used to give default value to the variable
        Adv = request.POST.get("des", "")  # second quote is used to give default value to the variable
        Banner=request.FILES.get("banner")
        x = publishad(name=Name, email=Email, mobile=Mobile,company=Cname,url=Url,advdes=Adv,banner=Banner)  #publishad is the table name/class name
        x.save()
        status = True
    return render(request,'thedailynewspaper/publish.html',{"s":status})
