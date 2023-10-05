# Walkthrough starting up Django Rest

1. pip install django
2. django-admin startproject drf_api .
3. pip install django-cloudinary-storage
4. pip install Pillow (passes image processing capabilities)
5. Add to installed apps in settings.py
6. Create env.py file
7. Add api-key to it
8. Import the env.py file into setting with:

import os

if os.path.exists('env.py'):
import env

CLOUDINARY_STORAGE = {
'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

9. Then we start our app with

python3 manage.py startapp profiles

10. Add this to installed apps in settings.py

11. Create the database model

12. Import Signal:

Examples of built-in Model signals include: pre_save, post_save, pre_delete and post_delete.
So, I’ll import post_save at the top from Django’s signals.
Now I’ll listen for the post_save signal coming from the User model by calling the connect function.
Inside, I’ll pass ‘create_profile’, which is the function I’d like to run every time  
and specify User as the model we’re expecting to receive the signal from.
Now we have to define the create_profile function before we pass it as an argument. Because we are  
passing this function to the post_save.connect method, it requires the following arguments:  
the sender model, its instance, created - which is a boolean value of whether or  
not the instance has just been created, and kwargs. Inside the create_profile function,  
if created is True, we’ll create a profile whose owner is going to be that user.

13. Then import it into the admin.py

from .models import Profile

admin.site.register(Profile)

14. Migrate

python3 manage.py makemigrations

python3 manage.py migrate

15. Create the superuser

python3 manage.py createsuperuser

16. After checking everything works, create requirements.txt

pip freeze > requirements.txt

## Django Rest framework

Now it is time to install Django Rest framework and continue.

1. Use prompt

pip install djangorestframework

2. Add it to installed apps

3. Create necessary code in views.py

"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile

class ProfileList(APIView):
def get(self, request):
profiles = Profile.objects.all()
return Response(profiles)

"""

4. Create a urls.py file in the app folder and add the url view.

5. Now let’s include profile urls in our main app. In the main urls.py, I’ll import ‘include’ from django urls and include profile urls at the bottom.

6. After all of this is made we need to create a serializer that transforms data format between JSON and Python code.
   We create a serializers.py file in the profiles app.

## Repetition

1. Create an app
2. Add the app to settings.py
3. Add the model to models.py
4. Migrate the models
5. Create serializer (import the model)
6. Create the view (import model and serializer)
7. Create app urls.py and add code
8. Add code to Django urls.py

Done

## Django Rest Auth

1. Install Django Rest Auth use

pip3 install dj-rest-auth==2.1.9 (for older version)

or

pip3 install dj-rest-auth

2. Then add following to settings.py

   'rest_framework.authtoken',
   'dj_rest_auth',

3. Add following to root urls.py

path('auth/', include('dj_rest_auth.urls')),

4. Then migrate database

5. Then install Django-allauth

pip3 install 'dj-rest-auth[with_social]'

6. Then we need to add the following to settings.py apps

'django-contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',

and also set

SITE_ID = 1
