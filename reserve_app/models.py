from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Office(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)

    def get_slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name


class Desk(models.Model):
    class Meta:
        unique_together = ('number', 'office')
    number = models.CharField(max_length=16)
    office = models.ForeignKey(Office, on_delete=models.CASCADE,
                               related_name='desks')

    def __str__(self):
        return f"{self.office} {self.number}"


class Reservation(models.Model):
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE,
                             related_name='reservations')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.desk.office.name} {self.desk.number} " \
               f"{self.user.username} {self.date}"
