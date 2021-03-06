from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# See https://docs.djangoproject.com/en/2.1/topics/db/models/ for details


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    reply = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    time_stamp = models.DateTimeField()
    image = models.TextField(null=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Post:" + str(self.id) + ", User: " + str(self.user) + ", Reply to: " + str(self.reply)


class Connection(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    active = models.BooleanField()

    def __str__(self):
        return "Connection:" + " User: " + str(self.sender) + " To: " + " User: " + str(self.receiver)
