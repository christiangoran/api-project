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

7. Then add the following line to root urls.py

   path('dj-rest-auth/', include('dj_rest_auth.urls')),

8. Then we have to install a simpel JWT library

pip3 install djangorestframework-simplejwt

First, we have to install the simple jwt library.
Because DRF doesn’t support JWT tokens for the browser interface  
out-of-the-box, we’ll need to use session authentication in development.
And for Production we’ll use Tokens.
This will allow us to continue to be able to log into our API as we work on it.

9. To make this distinction, I’ll set ‘DEV’ to ‘1’ in the env.py file.

10. Add this to settings.py to use the DEV-value to see if we are in development or production:

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
'rest_framework.authentication.TokenAuthentication'
if 'DEV' in os.environ else
'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
],

}

11. To enable token authentication, we’ll also have to set REST_USE_JWT to True.

and

To make sure they’re sent over HTTPS only, we will set JWT_AUTH_SECURE to True as well.

We also need to declare the cookie names for the access and refresh tokens, as we’ll be using both.

JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-app-refresh'

12. Create a serializer in Django folder and add following code:

from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CurrentUserSerializer(UserDetailsSerializer):
profile_id = serializers.ReadOnlyField(source='profile.id')
profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )

13. Now that we’ve created the file, let’s overwrite the default USER_DETAILS_SERIALIZER in settings.py.

REST_AUTH_SERIALIZERS = {
'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}

14. Finally, as we’ve finished installing everything, let’s run our migrations again.

Now JSON Web Tokens should be installed.

15. Since we installed new dependencies make a pip3 freeze > requirements.txt

## Add pagination

Add this to settings.py

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [(
'rest_framework.authentication.SessionAuthentication'
if 'DEV' in os.environ
else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
)],
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 10,
}

## Set JSON as default

Write this in settings.py

if 'DEV' not in os.environ:
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
'rest_framework.renderers.JSONRenderer',
]

## Change datetimeformat

settings.py:
'DATETIME_FORMAT': '%d %b %Y',

or for a different format on the time

serializers.py:
from django.contrib.humanize.templatetags.humanize import naturaltime

created_at = serializers.SerializerMethodField()
updated_at = serializers.SerializerMethodField()

def get_created_at(self, obj):
return naturaltime(obj.created_at)

def get_updated_at(self, obj):
return naturaltime(obj.updated_at)

Then I will get this format:

"created_at": "3 days, 16 hours ago",
"updated_at": "3 days, 16 hours ago",
