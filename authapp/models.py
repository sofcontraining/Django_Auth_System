from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return 'Enquiry From ' + self.name
