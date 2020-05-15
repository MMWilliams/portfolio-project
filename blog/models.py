from django.db import models

# Create your models here.
#models.Model = allows us to create the new job class, 
# #which allows the opbject ot be saved
#inside of the database we choose

class Blog(models.Model):
   #this wil be a blogpost
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')