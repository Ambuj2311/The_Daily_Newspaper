from django.db import models

# Create your models here.
#python manage.py makemigrations
#python manage.py migrate

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mob=models.CharField(max_length=20)
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.email

class category(models.Model):
    cname=models.CharField(max_length=20)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()

    def __str__(self):
        return self.cname

class register(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,primary_key=True)
    passwd=models.CharField(max_length=50)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=2000)

class news(models.Model):
    headlines = models.CharField(max_length=400)
    city=models.CharField(max_length=20)
    subject=models.CharField(max_length=800)
    newsdes=models.TextField(max_length=8000)
    newspic=models.ImageField(upload_to='static/news/',default="")
    ndate=models.DateField()
    ncategory=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.city

class notification(models.Model):
    ndes = models.TextField(max_length=5000)
    ndate=models.DateField()

class video(models.Model):
    vtitle=models.CharField(max_length=200)
    vdes=models.TextField(max_length=600)
    thumb=models.ImageField(upload_to='static/thumbnail/',default="")
    vlink=models.CharField(max_length=500)
    vdate=models.DateField()


class slider(models.Model):
    stitle=models.CharField(max_length=200)
    sdes=models.CharField(max_length=500)
    spic=models.ImageField(upload_to='static/slider/',default="")
    sdate=models.DateField()

class cities(models.Model):
       cityname=models.ForeignKey(news,on_delete=models.CASCADE)

class publishad(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    mobile = models.CharField(max_length=20)
    company=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    advdes=models.TextField(max_length=800)
    banner=models.ImageField(upload_to='static/publishbanner/',default="")

class world(models.Model):
    wheadlines = models.CharField(max_length=400)
    country = models.CharField(max_length=20)
    wsubject = models.CharField(max_length=800)
    wdes = models.TextField(max_length=8000)
    wpic = models.ImageField(upload_to='static/news/', default="")
    wdate = models.DateField()
    wcategory = models.ForeignKey(category, on_delete=models.CASCADE,default="8")

