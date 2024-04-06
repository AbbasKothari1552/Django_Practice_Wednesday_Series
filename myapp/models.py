from django.db import models

# Create your models here.

class Venue(models.Model):

    name = models.CharField('Venue Name',max_length = 100)
    address = models.CharField('Address of Venue',max_length= 300)
    pincode = models.IntegerField('Pincode')
    phone_no = models.IntegerField('Contact Number', blank= True)
    website = models.CharField('Website Address',max_length = 100, blank= True)
    email = models.EmailField('Email Address', blank= True)

    def __str__(self):
        return self.name
