from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

class Question(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    ques=models.TextField()

    def __str__(self) -> str:
        return self.ques
    def get_absolute_url(self):

        return reverse('details',kwargs={'pk':self.pk})

    

class Answer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    ques=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='questions')
    ans=models.TextField()

    def __str__(self) -> str:
        return self.ans
    
    
   



