from django.db import models
from django.contrib.auth.models import User

# Список сайтов
class Site(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
    	return self.title


class UserSite(models.Model):
    user = models.ForeignKey(User, related_name='user_related', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, related_name='site_related', on_delete=models.CASCADE)
    def __str__(self):
    	return self.user