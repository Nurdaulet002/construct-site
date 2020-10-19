from django.db import models

# Список сайтов
class Site(models.Model):
    title = models.CharField(max_length=120)
    
    class Meta:
        db_table='site'

    def __str__(self):
    	return self.title