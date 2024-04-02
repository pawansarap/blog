from django.db import models

# Create your models here.
class Contact (models.Model):
    # contact_id = models.AutoField(("Contact id"), primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name +' ('+self.email+')'

class Blog (models.Model):
    # blog_id = models.AutoField(("Contact id"), primary_key=True)
    blogtitle = models.CharField(max_length=200)
    blogemail = models.EmailField(max_length=150)
    blogdesc = models.TextField(max_length=500)
    blogthumbnail = models.ImageField(upload_to='images') 
    # print(blogtitle)
    # print(blogthumbnail) # Images will be uploaded to MEDIA_ROOT/images/
    blogdate = models.DateField()
    
    def __str__(self):
        return self.blogtitle +' ('+self.blogemail+')'