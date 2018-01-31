# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from..login.models import User
from django.db import models

# Create your models here.
class QuoteManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['message']) < 5:
            errors.append("Message field must be 5 characters or more")
        if len(post_data['message']) < 30:
            errors.append("Message field must be 30 characters or more")
        return errors

class Quote(models.Model):
    quoted_by = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="quotes_created", default=1)
    user_favorites = models.ManyToManyField(User, related_name="favorites")
    # user_favorites = models.ForeignKey(User, related_name="favorite")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = QuoteManager()
