from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField("Text", max_length=128)
    done = models.BooleanField("Done", default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"