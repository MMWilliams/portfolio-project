from django.db import models

# Create your models here.
#models.Model = allows us to create the new job class, 
# #which allows the opbject ot be saved
#inside of the database we choose

class Job(models.Model):
    #whenever an image is uploaded, where is is saved to
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.summary