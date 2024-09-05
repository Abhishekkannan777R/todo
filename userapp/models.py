from django.db import models



class regtb2(models.Model):
    taskname=models.CharField(max_length=20)
    taskdate=models.DateField()
     