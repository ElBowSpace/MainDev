from django.db import models


# Create your models here.
# See https://docs.djangoproject.com/en/2.1/topics/db/models/ for details
class User(models.Model):
    id = models.AutoField(primary_key=True)  # <-- this is included by default in all models
    connection = models.ManyToManyField('self')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    time_stamp = models.DateTimeField()
    image = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Post:" + str(self.id) + ", User: " + str(self.user) + ", Reply to: " + str(self.reply)
