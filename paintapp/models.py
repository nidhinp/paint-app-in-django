from django.db import models

# Create your models here.


class Files(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField()
    canvas_image = models.TextField()
    
    def __unicode__(self):
        return self.name
    
