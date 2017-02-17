from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9_+.-]+@[a-zA-Z0-9_+.-]+\.[a-zA-Z]+')



class UserManager(models.Manager):
    def create_new_user(self, data):
        errors = []

        print "i'm getting passed this, ", data

        if len(data['first_name']) < 2:
            errors.append('First name must be at least one character')
        #
        # if not re.match(data['email'], EMAIL_REGEX):
        #     errors.append('Email must be valid')

        if errors:
            return (False, errors)

        else:
            house_obj = House.objects.get(name=data['house'])


            new_user = User.objects.create(
                first_name=data['first_name'],
                house=house_obj,
                weapon=data['weapon'],
                evil_scale=int(data['evil_scale']),
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.first_name


class Region(models.Model):
    name = models.CharField(max_length=200)
    houses = models.ForeignKey(House, related_name="home_region")
    climate = models.CharField(max_length=200)
    known_for = models.CharField(max_length=200)
    #adjacent_region
