from __future__ import unicode_literals

from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class User_manager(models.Manager):
    def user_manager(self, post_data):
        print('--------------MANAGER VALIDATING----------')
        print(post_data)
        response_to_views = {}
        errors = []
        if len(post_data['name']) < 1:
            errors.append('Name required')
        if len(post_data['username']) < 1:
            errors.append("Username required")
        if len(post_data['rpassw_confirm']) < 1:
            errors.append("Password Confirmation required")
        if not post_data['rpassw'] == post_data['rpassw_confirm']:
            errors.append("Passwords must match")
        if self.filter(username =post_data['username']):
            errors.append('Username is already in use')
        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:
            response_to_views['status'] = True
            print ('--------------APPROVED------------')
            hashed_password = bcrypt.hashpw(post_data['rpassw'].encode(), bcrypt.gensalt())
            user = self.create(name = post_data['name'], username = post_data['username'], password= hashed_password )
            response_to_views['user'] = self.name

            print ('--------------USER ADDED--------------')
        return response_to_views
    def login_user(self, post_data):
        print('---------------VALIDATING LOGIN----------')
        response_to_views = {}
        user = self.filter(username = post_data['username'])
        print(user)
        if user:
            if bcrypt.checkpw(post_data['lpassw'].encode(), user[0].password.encode()):
                response_to_views['status'] = True
                response_to_views['user'] = user[0]
            else:
                response_to_views['status'] = False
                response_to_views['errors'] = 'Invalid Username/Password'
        else:
            response_to_views['status'] = False
            response_to_views['errors'] = 'Invalid Entry'
        return response_to_views
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()
