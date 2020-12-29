from django.db import models

# Create your models here.
class Trainer(models.Model):
    """
    This class represents the Pomemon Trainer itself.
    """
    name = models.CharField(max_length=20, null=False, default="Red")
    last_name = models.CharField(max_length=100, null=False, default="Oak (lmao)")
