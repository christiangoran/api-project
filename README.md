# Django Rest

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

## DEPLOYMENT

1. Login to ElephantSQL.com and create a new instance. Copy the url from the newly created instance.
2. Login to Heroku and create a new app

   1. Afterwards go to settings and enter following in config vars:

   DATABASE\*URL : "postgres://yotnuypp:WwDkSCsYr**\*\***\*\*\***\*\***\***\*\***\*\***\*\***"

3. In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database

pip3 install dj_database_url==0.5.0 psycopg2

4. In your settings.py file, import dj_database_url underneath the import for os

import os
import dj_database_url

5. Update the DATABASES section to the following

if 'DEV' in os.environ:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}
else:
DATABASES = {
'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

This will ensure that when you have an environment variable for DEV in your environment the code will connect to the sqlite database here in your IDE. Otherwise it will connect to your external database, provided the DATABASE_URL environment variable exist.

6. In your env.py file, add a new environment variable with the key set to DATABASE_URL, and the value to your ElephantSQL database URL

os.environ['DATABASE_URL'] = "<your PostgreSQL URL here>"

7. Temporarily comment out the DEV environment variable so that your IDE can connect to your external database

os.environ['CLOUDINARY_URL'] = "cloudinary://..."
os.environ['SECRET_KEY'] = "Z7o..."
'# os.environ['DEV'] = '1'
os.environ['DATABASE_URL'] = "postgres://..."

8. Back in your settings.py file, add a print statement to confirm you have connected to the external database

if 'DEV' in os.environ:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}
else:
DATABASES = {
'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
print('connected')

9. In the terminal, -–dry-run your makemigrations to confirm you are connected to the external database

python3 manage.py makemigrations --dry-run

If you are, you should see the ‘connected’ message printed to the terminal

10. Remove the print statement

11. Migrate your database models to your new database

12. Create a superuser for your new database

python3 manage.py createsuperuser

### Confirmation that database was created

1. On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”

2. Click the Table queries button, select auth_user

3. When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database

### Preparing for deployment

Now that your external database has all its tables and a superuser, we will prepare your project for deployment to Heroku. This will include installing a package needed to run the project on Heroku, fixing a few environment variables, and creating a Procfile file that will provide the commands to Heroku to build and run the project.

1. In the terminal of your IDE workspace, install gunicorn

pip3 install gunicorn django-cors-headers

2. Update your requirements.txt

pip3 freeze > requirements.txt

3. As you may remember from previous projects, Heroku also requires a Procfile. Create this file now. Remember, it must be named correctly and not have any file extension, otherwise Heroku won’t recognise it

Inside the Procfile write these two commands;

release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi

4. In your settings.py file, update the value of the ALLOWED_HOSTS variable to include your Heroku app’s URL

ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']

5. Add corsheaders to INSTALLED_APPS

INSTALLED_APPS = [
...
'dj_rest_auth.registration',
'corsheaders',
...
]

6. Add corsheaders middleware to the TOP of the MIDDLEWARE

SITE_ID = 1
MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
...
]

7. Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:

if 'CLIENT_ORIGIN' in os.environ:
CORS_ALLOWED_ORIGINS = [
os.environ.get('CLIENT_ORIGIN')
]
else:
CORS_ALLOWED_ORIGIN_REGEXES = [
r"^https://.*\.gitpod\.io$",
]

_info_

Here the allowed origins are set for the network requests made to the server. The API will use the CLIENT_ORIGIN variable, which is the front end app's url. We haven't deployed that project yet, but that's ok. If the variable is not present, that means the project is still in development, so then the regular expression in the else statement will allow requests that are coming from your IDE.

### Deployment

With those changes in place, we can now deploy our project to Heroku.

1. Back on the Heroku dashboard for your new app, open the Settings tab

2. Add two more Config Vars:

   SECRET_KEY (you can make one up, but don’t use the one that was originally in the settings.py file!)

   CLOUDINARY_URL, and for the value, copy in your Cloudinary URL from your env.py file (do not add quotation marks!)

3. Open the Deploy tab
4. In the Deployment method section, select Connect to GitHub
5. Search for your repo and click Connect

6. As we already have all our changes pushed to GitHub, we will use the Manual deploy section and click Deploy Branch.

### Fix dj-rest-auth bug

Problem Statement

It turns out that dj-rest-auth has a bug that doesn’t allow users to log out (ref: DRF Rest Auth Issues).

The issue is that the samesite attribute we set to ‘None’ in settings.py (JWT_AUTH_SAMESITE = 'None') is not passed to the logout view. This means that we can’t log out, but must wait for the refresh token to expire instead.
Proposed Solution

One way to fix this issue is to have our own logout view, where we set both cookies to an empty string and pass additional attributes like secure, httponly and samesite, which was left out by mistake by the library.

Follow the steps below to fix this bug

1. In drf_api/views.py, import JWT_AUTH settings from settings.py.

from .settings import (
JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
JWT_AUTH_SECURE,
)

2. Write a logout view. Looks like quite a bit, but all that’s happening here is that we’re setting the value of both the access token (JWT_AUTH_COOKIE) and refresh token (JWT_AUTH_REFRESH_COOKIE) to empty strings. We also pass samesite=JWT_AUTH_SAMESITE, which we set to ’None’ in settings.py and make sure the cookies are httponly and sent over HTTPS,

@api_view(['POST'])
def logout_route(reguest):
response = Response()
response.set_cookie(
key=JWT_AUTH_COOKIE,
value='',
httponly=True,
expires='Thu, 01 Jan 1970 00:00:00 GMT',
max_age=0,
samesite=JWT_AUTH_SAMESITE,
secure=JWT_AUTH_SECURE,
)
response.set_cookie(
key=JWT_AUTH_REFRESH_COOKIE,
value='',
httponly=True,
expires='Thu, 01 Jan 1970 00:00:00 GMT',
max_age=0,
samesite=JWT_AUTH_SAMESITE,
secure=JWT_AUTH_SECURE,
)
return response

#### Step 2 urls.py

3. Now that the logout view is there, it has to be included in drf_api/urls.py . The logout_route also needs to be imported,

from .views import root_route, logout_route

4.  ... and then included in the urlpatterns list. The important thing to note here is that our logout_route has to be placed above the default dj-rest-auth urls, so that it is matched first.

path('dj-rest-auth/logout/', logout_route),

5. Push to Github and redeploy with Heroku
