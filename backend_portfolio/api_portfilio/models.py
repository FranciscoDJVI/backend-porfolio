from django.db import models


class Email(models.Model):
    email_contact = models.CharField(max_length=150, blank=False, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.email_contact

