import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '08de9034602fdb0892f5ea0048e6c9a8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()


    cities = City.objects.all()



    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()
        print(url.format(city.name))
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        print(city.name)

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form':form}
    # context = {'info': city_info}
    return render(request, 'weather/index.html', context)
