# Direct Supply Kata Problem 2  -  Weather API
# Josiah Mathews - MSOE Computer Science Student

from tabulate import tabulate   # Nice table formatting!
import requests   # API Calls thorough requests

# Note: This API Key MAY need to be changed per tester for updated API access!
#        Please sign up on the website: https://api.openweathermap.org to gain the quick API iff need be.
API_KEY = '9030a27dd426ba57c5700baaf9bf2043'

GEO_URL = 'https://api.openweathermap.org/geo/1.0/direct?q='  #GEO API for City name rather than Long/Lat params [same source]
LAT_LONG_URL = 'https://api.openweathermap.org/data/2.5/weather?'  #Standard API for found Long/Lat params [same source]

"""
"""
def get_lat_lon(city):
    # TODO TRY to Grab city's Longitude and Latitude from GEO API
    # TODO add check and Clean Response
    response = requests.get(GEO_URL + city + '&limit=1' + '&appid=' + API_KEY)

    if response.status_code == 200:  # successful API Call
        # Parse only Longitude and Latitude from valid City!
        lat = str(response.json()[0]['lat'])
        lon = str(response.json()[0]['lon'])
        return lat, lon

    return None, None


"""
"""
def get_weather(latitude, longitude):
    # TODO TRY to Call API with valid lat & lon from specific City
    response = requests.get(LAT_LONG_URL + "&lat=" + latitude + "&lon=" + longitude + '&appid=' + API_KEY + '&units=imperial')   # imperial Units = Fahrenheit according to API JSON Fields

    if response.status_code == 200:
        # Output Features? Vague descriptions but will GRAB best JSON Options?
        json_data = response.json()
        city = json_data['name']
        temp = json_data['main']['temp']
        temp_high = json_data['main']['temp_max']
        temp_low = json_data['main']['temp_min']
        humidity = json_data['main']['humidity']  # %
        type = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']

        # Prepare table data
        table = [
            ["City", city],
            ["Condition", type],
            ["Temperature (°F)", temp],    # just found out to type Alt + 0176 for Degree Symbol
            ["Min. (LOW) Temperature (°F)", temp_low],
            ["Max (HIGH) Temperature (°F)", temp_high],
            ["Humidity (%)", humidity],
            ["Description", description.capitalize()]
        ]

        # OUTPUT very organized to TABULATE using parsed, ordered table data above
        return tabulate(table, headers=["Weather Detail", "Current Value"], tablefmt="grid")  # could also print individual OUTPUT

    return None  # API Error


# TODO Add main input() method!!
# Script 'Main' method
if __name__ == '__main__':
    city = input('Enter City: ')
    latitude, longitude = get_lat_lon(city)

    if latitude and longitude: #not null
        table = get_weather(latitude, longitude)

        if table:
            print(table)
        else:
            print("Error fetching City's Weather data.")
    else:
        print("City not found.")


# TODO update README with .venv instructions and overall output
# TODO create TESTS?
