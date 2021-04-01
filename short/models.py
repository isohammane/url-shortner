import short
from django.db import models
import random ,string

def unique_link():
    length =random.randint(1,6) 
    while True:
        link = ''.join(random.choices(string.ascii_letters ,k=length))
        if Link.objects.filter(short=link).count() == 0:
            break
    return link

# Create your models here.
class Link(models.Model):
    original = models.CharField(max_length=500,null=True)
    short = models.CharField(max_length=8,default=unique_link)

    def __str__(self):
        return self.original