from django.db import models

# Create your models here.

class AIReport(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    generated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
