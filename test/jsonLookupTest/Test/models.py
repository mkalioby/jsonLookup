from django.db import models
from django.db.models.fields import Field
from jsonfield import JSONField

from jsonLookup import hasLookup

JSONField.register_lookup(hasLookup)


class User(models.Model):
    name=models.CharField(max_length=50)
    properties=JSONField()


# Create your models here.
