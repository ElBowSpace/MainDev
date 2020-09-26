from django.db import models


# Create your models here.
# See https://docs.djangoproject.com/en/2.1/topics/db/models/ for details
class User(models.Model):
    id = models.AutoField(primary_key=True)  # <-- this is included by default in all models
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name


class Connection(models.Model):
    user1 = models.ForeignKey(User.id, primary_key=True, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User.id, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user1) + str(self.user2)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=255)
    time_stamp = models.DateTimeField()
    image = models.TextField(max_length=255)
    user = models.ForeignKey(User.id, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Post):
    post = models.ForeignKey(Post.id, on_delete=models.CASCADE)
