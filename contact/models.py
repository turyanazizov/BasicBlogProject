from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(blank=False,null=False)
    number=models.CharField(max_length=100,blank=False,null=False)
    select=models.CharField(max_length=100,blank=False,null=False)
    text=models.TextField(blank=False,null=False)

    def __str__(self):
        return self.name

