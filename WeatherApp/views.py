from django.shortcuts import render
import requests
import json

API_KEY =""
def kelvin_to_celsius(kelvin):
    return int(kelvin - 273.15)

def app(request):
    city = request.GET.get('city', '')  # Get the city value from dropdown
    city_text = request.GET.get('city_text', '')  # Get the city value from input text
    
    if city or (city_text and city_text.isalpha()):  # If a city is selected from dropdown or entered in text
        if city:  # If city is selected from dropdown
            resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
        else:  # If city is entered in text
            resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_text}&appid={API_KEY}')
        
        if resp.status_code == 200:
            data = resp.json()
            city_name = data['name']
            weather = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature_kelvin = data['main']['temp']
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)  # Convert temperature to Celsius
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            
            context = {
                'city_name': city_name,
                'weather': weather,
                'description': description,
                'temperature': temperature_celsius,  # Pass temperature in Celsius
                'pressure': pressure,
                'humidity': humidity
            }
            
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', {'data': 'Failed to fetch weather data'})
    else:
        return render(request, 'index.html')
