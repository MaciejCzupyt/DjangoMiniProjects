from django.db import models
from django.core.validators import validate_email


class ExampleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.CharField(default='example@example.com', validators=[validate_email])

    def __str__(self):
        return self.title


class OtherModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.description
