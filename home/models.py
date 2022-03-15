from django.db import models

class Projects(models.Model):
    main_content = models.TextField( blank=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

    def __str__(self):
        return 'All Projects content'

class SingleProject(models.Model):
    project_name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100,blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    agency = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    image1 = models.ImageField(upload_to='projects/', null=False, blank=False,)
    image2 = models.ImageField(upload_to='projects/', null=False, blank=False,)
    image3 = models.ImageField(upload_to='projects/', null=False, blank=False,)

    class Meta:
        verbose_name = 'Single Project'
        verbose_name_plural = 'Single Projects'

    def __str__(self):
        return self.project_name