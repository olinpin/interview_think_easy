from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField("Title", max_length=128, blank=True)
    text = models.CharField("Text", max_length=128, blank=True)
    done = models.BooleanField("Done", default=False, blank=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"

#User.add_to_class('new_field', models.(Tasks, blank=True, null=True,  on_delete=models.CASCADE))