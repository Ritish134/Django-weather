from django.shortcuts import render
import json
import urllib.request

# Start from scratch
# django-admin startproject projectName
# cd projectName
# python manage.py startapp feature
# create a folder templates for html files
# in settings.py 'DIRS': [BASE_DIR/'templates'],
# also in installed apps write weather
# create urls.py in feature folder created
## in that file from django.urls import path
### from . import views
#### urlpatterns = [
#     path('',views.index,name='index')
# ]
# Now in views.py here below create index

# in urls.py in main project 

# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('weather.urls'))
# ]

# to run server python manage.py runserver
# create a index.html file in templates folder
# add {% csrf_token %}if using post method
# python manage.py makemigrations if u did changes in models.py
# python manage.py migrate
# python manage.py createsuperuser >>to create admin

# searilizer -> django models to json data



# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=fc1d15914c5b9dbe2f021b2f35c7c567').read()
        json_data = json.loads(res)

        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }

    else:
        data = {}
    return render(request,'index.html',data)