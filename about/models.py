from pyexpat import model
from django.db import models

class AboutMain(models.Model):
    Main_Title = models.CharField(max_length=50, blank=False, null=False)
    Main_Content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/', null=False, blank=False,)
    Title = models.CharField(max_length=50, blank=False, null=False)
    First_Text = models.TextField(blank=True, null=True)
    Second_Text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Main'
        verbose_name_plural = 'Main'

    def __str__(self):
        return 'Main About fields'

class AboutSubject(models.Model):
    Subject = models.CharField(max_length=50, blank=False, null=False)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=100, blank=True, null=True)
    text4 = models.CharField(max_length=100, blank=True, null=True)
    text5 = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ('date', )
    
    def __str__(self):
        return self.Subject