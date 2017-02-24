from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9_+.-]+@[a-zA-Z0-9_+.-]+\.[a-zA-Z]+')
PW_REGEX = re.compile(r'[A-Z]+[a-z]+|[a-z]+[A-Z]+')


class UserManager(models.Manager):
    def create_new_user(self, data):
        errors = []

        print "i'm getting passed this, ", data

        if not len(data['first_name']):
            errors.append('First name must be at least one character')

        try:
            evil_scale = int(data['evil_scale'])
        except:
            errors.append('Evil scale must be an integer')

        if not len(data['weapon']):
            errors.append('Weapon must be filled')

        if not 'house' in data:
            errors.append('Person must be given a House')

        if len(data['password']) < 8:
            errors.append('Password is too short, must be at least 8 characters')
        elif not re.match(PW_REGEX, data['password']):
            errors.append('Password must contain both upper and lower case letters')

        if errors:
            return (False, errors)

        else:
            house_obj = House.objects.get(name=data['house'])
            pw = data['password'].encode()
            pw_hash = bcrypt.hashpw(pw, bcrypt.gensalt())

            new_user = User.objects.create(
                first_name=data['first_name'],
                house=house_obj,
                weapon=data['weapon'],
                evil_scale=evil_scale,
                password=pw_hash
            )
            return (True, new_user)



class House(models.Model):
    name = models.CharField(max_length=200)
    words = models.CharField(max_length=200)
    banner = models.CharField(max_length=200)
    color_1 = models.CharField(max_length=200)
    color_2 = models.CharField(max_length=200)
    #home_region
    #members

    def __str__(self):
        return "<house object" + self.name + ">"

class User(models.Model):
    first_name = models.CharField(max_length=200)
    house = models.ForeignKey(House, related_name="members")
    weapon = models.CharField(max_length=200)
    evil_scale = models.IntegerField(null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.first_name
