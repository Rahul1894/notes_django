from django.db import models # type: ignore
from django.contrib.auth.models import User #type:ignore
# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=200)
    notes=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="notes")
