# ElbowSpace Data Models

## ElbowSpace Data

Data Classes and database tables

* User
    * id
    * first_name
    * last_name
    * email
    * password
    * active
  
* Post
    * id
    * body
    * time_stamp
    * image
    * user.id*
     
* Comment
    * Post.id*

* Connection
  * user1
  * user2


  


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
    from django.contrib.auth.models import User

    class User(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)

    class Post(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)

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
    