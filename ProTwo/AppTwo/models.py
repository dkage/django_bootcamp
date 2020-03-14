from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        # This decorator is used to show a value in admin panel for this model. Otherwise it shows "User object(<X>)"
        return str(self.first_name + ' ' + self.last_name)
