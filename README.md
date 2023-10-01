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
