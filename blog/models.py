from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    description = RichTextUploadingField(blank=True,null=True)
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    def __str__(self):
        return self.title #제목으로 보이게
    
    def summary(self):
        return self.body[:100]