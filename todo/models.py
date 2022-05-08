from django.db import models 

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # to update the name of the new item as without this it give a,
    # standard object name to our item
    def __str__(self):
        return self.name
