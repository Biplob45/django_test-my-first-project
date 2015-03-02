from django.db import models
from datetime import time  #15th video

def get_upload_file_name(instance, filename):  #15th video ar jonno pera
    return "uploaded_files/%s_%s" %(str(time()).replace('.','_'),filename)

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date=models.DateTimeField('date published')
    likes = models.IntegerField(default=0)  #12th video te default = 0 dile kaj kore
    
    thumbnail = models.FileField(upload_to=get_upload_file_name)  #15th video te..........
    
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")
    article = models.ForeignKey(Article)