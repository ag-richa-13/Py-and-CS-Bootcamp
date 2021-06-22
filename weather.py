# Import required moidule
import requests, json
#import datetime
from datetime import datetime

# Enter api id and city name
api_key = '87d845b0b6cf29baa1a73cc34b067a95'
city_name = input("Enter City Name: ")
# base url
base_url = "https://api.openweathermap.org/data/2.5/weather?"


data = requests.get(base_url+f"q={city_name}&units=metric&APPID={api_key}")

#create date variable

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("---------------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city_name.upper(), date_time))
print ("---------------------------------------------------------------------")
print("--------------------------------------------")
# print(data.json())
# getting the data
print(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
print(f"Temperature: {data.json().get('main')['temp']}°C")
print(f"Weather: {data.json().get('weather')[0].get('main')}")
print(
    f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C"
)
print(f"Humidity: {data.json().get('main')['humidity']}%")
print(f"Wind: {data.json().get('wind')['speed']} km/h")
print("--------------------------------------------")