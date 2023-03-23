from django.db import models

# Create your models here.
class ProblemSet(models.Model):
    title = models.CharField(max_length=100)
    due = models.DateField()
