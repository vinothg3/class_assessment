from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

class Question(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=200)

    def get_abolute_url(self):
        return reverse('answers',kwargs={'pk':self.pk })
    
    def __str__(self) -> str:
        return self.question
class Allanswer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='allans')
    answer=models.CharField(max_length=100)