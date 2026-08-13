from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    field = models.CharField(max_length=100)
    gender = models.CharField(
    max_length=10,
    choices=[
        ("M", "Male"),
        ("F", "Female"),
    ]
)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name 