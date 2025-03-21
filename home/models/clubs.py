from django.db import models
from home.models import Person


class Club(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(to=Person, related_name="clubs", blank=True)
    memberships = models.ManyToManyField(
        to=Person, through="Membership", related_name="memberships", blank=True
    )


class Membership(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    member = models.ForeignKey(Person, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    expiry = models.DateTimeField(blank=True, null=True)
