# Django Weather App

This is a simple Django web application that fetches and displays weather information for a given city using the OpenWeatherMap API.

## Features

- Allows users to select a city from a dropdown menu or enter a city name manually.
- Displays weather information including:
  - City name
  - Current weather condition
  - Description
  - Temperature in Celsius
  - Pressure
  - Humidity

## Features
- Select a city from the dropdown menu or enter a city name manually in the input field.
- Click on the "Submit" button.
- Weather information for the selected city will be displayed on the page.
-Technologies Used
 - Python
 - Django
 - HTML
 - CSS
 - OpenWeatherMap API


## Setup

1. Clone the repository:

```bash
git clone <repository_url>
cd django-weather-app

-----
Create and activate a virtual environment (optional but recommended):
pip install -r requirements.txt

- Obtain an API key from OpenWeatherMap by signing up at https://home.openweathermap.org/users/sign_up.
- Replace 'YOUR_API_KEY' in app/views.py with your actual API key obtained from OpenWeatherMap:
resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY')

-Run the Django server:
python manage.py runserver




