from __future__ import unicode_literals

from django.db import models
from datetime import date
from ..login.models import User
# Create your models here.

class Destination_manager(models.Manager):
    def d_manager(self, post_data):
        print('--------------MANAGER VALIDATING--')
        response_to_views = {}
        errors = []
        if len(post_data['name']) < 1:
            errors.append("Name required")
        if len(post_data['desc']) < 1:
            errors.append("Description required")
        if len(post_data['td_from']) < 1:
            errors.append("Start Date required")
        if len(post_data['td_to']) < 1:
            errors.append("End Date required")
        if post_data['td_to']>post_data['td_from']:
            errors.append("Your dates are jacked up!")
        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:
            response_to_views['status'] = True
            print ('--------------APPROVED------------')

            destination = self.create(name = post_data['name'], desc = post_data['desc'], td_from = post_data['td_from'], td_to = post_data['td_to'])
            print ('--------------  ADDED ------------')

            user = User.objects.last()
            destination.users.add(user)
            
            print ('--------------  RELATIONSHIP MADE-')
        return response_to_views
class Destination(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    td_from = models.DateField()
    td_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="destinations")
    objects = Destination_manager()
