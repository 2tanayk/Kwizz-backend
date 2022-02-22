from django.db import models

# Create your models here.
class Question(models.Model):
    quesId = models.CharField(max_length=50)
    question = models.CharField(max_length=200)

class Options(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE, related_name='options', primary_key=True)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)

class Answer(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE, related_name='answer', primary_key=True)
    answer=models.CharField(max_length=50)

class SubmittedAnswer(models.Model):
    question=models.OneToOneField(Question,on_delete=models.CASCADE, related_name='submission', primary_key=True)
    submittedAnswer=models.CharField(max_length=50)


