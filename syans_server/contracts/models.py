from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contract(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField()
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.CASCADE)
    cost = models.IntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return '{} ({} -> {} : {}$)'.format(self.title, self.customer, self.executor, self.cost)