from email.policy import default
from secrets import choice
from django.db import models


class User(models.Model):
    PARENT = "P"
    CHILD = "C"
    ROLES = [
        (PARENT, "Parent"),
        (CHILD, "Child"),
    ]
    name = models.TextField()
    email = models.EmailField()
    role = models.TextField(choices=ROLES)


class Chart(models.Model):
    child = models.ForeignKey("User", on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    modified = models.DateTimeField("Last modified date time", auto_now=True)
    modified_by = models.ForeignKey(
        "User", on_delete=models.SET_NULL, blank=True, null=True, related_name="+"
    )
    members = models.ManyToManyField(User, related_name="members")
