from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/images/', null=True, blank=True)
    mobile_no = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

