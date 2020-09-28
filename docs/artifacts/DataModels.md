# ElbowSpace Data Models

## ElbowSpace Data

Data Classes and database tables

* User
    * id
    * connection
    * first_name
    * last_name
    * email
    * password
    * active
  
* Post
    * id
    * reply
    * body
    * time_stamp
    * image
    * user.id*
     
     
"*" indicates a foreign key 

Example: User make Posts so the psot data model has
a ForeignKeyField that points to the user Model class.

#### Post/models.py

ElbowSpace/settings.py

    INSTALLED_APPS = [
        ...
        'MainApp',
    ]

MainApp/models.py

    from django.db import models

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

Migrate the database

    python manage.py makemigrations
    
    python manage.py migrate
 
 
## Django Admin Views

Enable the admin views

MainApp/urls.py

    from django.urls import path
    from django.contrib import admin
    
    urlpatterns = [
        ...
        path(r'admin/', admin.site.urls),
    ]
    

MainApp/admin.py

    from django.contrib import admin
    from .models import User, Post

    admin.site.register(User)
    admin.site.register(Post)

Create Superuser to use admin views

    python manage.py createsuperuser
    
    python manage.py runserver
    
Browse to test

    Visit http://127.0.0.1:8002/admin/
    