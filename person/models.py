from django.db import models


class Person(models.Model):
    SEX_CHOICES = (
        ("F", "Female"),
        ("M", "Male"),
        ("O", "Other")
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    rg = models.CharField(max_length=20, null=False, blank=False)
    cpf = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    birthdate = models.DateField(null=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)

    def __str__(self):
        return f'Person {self.name}'
