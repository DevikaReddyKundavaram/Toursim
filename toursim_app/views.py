

from django.shortcuts import render, get_object_or_404,redirect
from .models import State_details, City,Place,HeritageSite,Location
# from django.http import HttpResponseNotAllowed

import requests
import math
def index(request):
    nearby_places = Place.objects.all()
    heritage_sites = HeritageSite.objects.all()
    states = State_details.objects.all()

    context = {
        'nearby_places': nearby_places,
        'heritage_sites': heritage_sites,
        'states': states,
    }

    return render(request, 'toursim_app/index.html', context)

def state(request, state_name=None):
    if request.method == 'GET':
        if state_name:
            state_obj = get_object_or_404(State_details, state_name=state_name)
            cities = City.objects.filter(state_id=state_obj.state_id)

            context = {
                'state': state_obj,
                'cities': cities,
            }

            return render(request, 'toursim_app/State.html', context)
        else:
            # Display the initial form
            return render(request, 'toursim_app/index.html')

    elif request.method == 'POST':
        # Handle the form submission
        query = request.POST.get('state_name', '')
        # Adjust the form input name as needed

        if query:
            # Redirect to the appropriate URL based on the form input
            return redirect('state_detail', state_name=query)
        else:
            # Display an error message if no state_name is provided
            return render(request, 'toursim_app/index.html', {'error_message': 'Please provide a state name'})

def city(request, city_name=None):
    if request.method == 'GET':
        if city_name:
            city_obj = get_object_or_404(City, city_name=city_name)
            locations= Location.objects.filter(city_id=city_obj.city_id)

            context = {
                'cities': city_obj,
                'locations': locations,
            }

            return render(request, 'toursim_app/City.html', context)
        else:
            # Display the initial form
            return render(request, 'toursim_app/State.html')

    elif request.method == 'POST':
        # Handle the form submission
        query = request.POST.get('city_name', '')
        # Adjust the form input name as needed

        if query:
            # Redirect to the appropriate URL based on the form input
            return redirect('city', city_name=query)
        else:
            # Display an error message if no state_name is provided
            return render(request, 'toursim_app/State.html', {'error_message': 'Please provide a state name'})




# def location(request, location_name=None):
#     if request.method == 'GET':
#         if location_name:
#             location_obj = get_object_or_404(Location, location_name=location_name)
#             # locations= Location.objects.filter(city_id=city_obj.city_id)
#
#             context = {
#                 'location': location_obj,
#                 # 'locations': locations,
#             }
#
#             return render(request, 'toursim_app/location.html', context,'toursim_app/weather_api/home.html')
#         else:
#             # Display the initial form
#             return render(request, 'toursim_app/City.html')
#
#     elif request.method == 'POST':
#         # Handle the form submission
#         query = request.POST.get('location_name', '')
#         # Adjust the form input name as needed
#
#         if query:
#             # Redirect to the appropriate URL based on the form input
#             return redirect('location', location_name=query)
#         else:
#             # Display an error message if no state_name is provided
#             return render(request, 'toursim_app/City.html', {'error_message': 'Please provide a state name'})

def location(request, location_name=None):
    if request.method == 'GET':
        if location_name:
            location_obj = get_object_or_404(Location, location_name=location_name)
            city_id = location_obj.city_id  # Assuming you have a 'city_id' field in your Location model
            nearby_locations = Location.objects.filter(city_id=city_id).exclude(location_name=location_name)

            context = {
                'location': location_obj,
                'nearby_locations': nearby_locations,
            }

            return render(request, 'toursim_app/location.html', context)
        else:
            # Display the initial form
            return render(request, 'toursim_app/City.html')

    elif request.method == 'POST':
        # Handle the form submission
        query = request.POST.get('location_name', '')

        if query:
            # Redirect to the appropriate URL based on the form input
            return redirect('location', location_name=query)
        else:
            # Display an error message if no location_name is provided
            return render(request, 'toursim_app/City.html', {'error_message': 'Please provide a location name'})




def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        w_dataset = requests.get(url).json()
        try:
            context = {
                ####
                "city_name":w_dataset["city"]["name"],
                "city_country":w_dataset["city"]["country"],
                "wind":w_dataset['list'][0]['wind']['speed'],
                "degree":w_dataset['list'][0]['wind']['deg'],
                "status":w_dataset['list'][0]['weather'][0]['description'],
                "cloud":w_dataset['list'][0]['clouds']['all'],
                'date':w_dataset['list'][0]["dt_txt"],
                'date1':w_dataset['list'][1]["dt_txt"],
                'date2':w_dataset['list'][2]["dt_txt"],
                'date3':w_dataset['list'][3]["dt_txt"],
                'date4':w_dataset['list'][4]["dt_txt"],
                'date5':w_dataset['list'][5]["dt_txt"],
                'date6':w_dataset['list'][6]["dt_txt"],


                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(w_dataset["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(w_dataset["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(w_dataset["list"][6]["main"]["temp_max"] -273.0),


                "pressure":w_dataset["list"][0]["main"]["pressure"],
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "sea_level":w_dataset["list"][0]["main"]["sea_level"],


                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],
                "icon":w_dataset["list"][0]["weather"][0]["icon"],
                "icon1":w_dataset["list"][1]["weather"][0]["icon"],
                "icon2":w_dataset["list"][2]["weather"][0]["icon"],
                "icon3":w_dataset["list"][3]["weather"][0]["icon"],
                "icon4":w_dataset["list"][4]["weather"][0]["icon"],
                "icon5":w_dataset["list"][5]["weather"][0]["icon"],
                "icon6":w_dataset["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')






