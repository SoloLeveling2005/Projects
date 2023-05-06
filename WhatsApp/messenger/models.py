from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

class User(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('name',)


class Message(models.Model):

    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
