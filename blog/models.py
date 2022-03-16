from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/', null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    creator_name = models.CharField(max_length=100, blank=False, null=False)
    creator_img = models.ImageField(upload_to='creators/', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    # Blogun Post url ucun olan Fieldler.
    second_title = models.CharField(max_length=255, null=False, blank=False)
    second_content = models.TextField(null=False, blank=False)
    creator_bio = models.TextField(null=False, blank=False)
    creator_job = models.CharField(max_length=105, null=False, blank=False)
    # comment = models.ForeignKey('Coment', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def __str__(self):
        return f"{self.creator_name}'s Blog"