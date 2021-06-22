# Import required moidule
import requests, json
#import datetime
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
city_name = input("Enter City Name: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "q="+city_name+"&appid="+api_key
api_link = requests.get(complete_url)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("---------------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city_name.upper(), date_time))
print ("---------------------------------------------------------------------")
print("----------------------------------------------------------")
print ("Current Temperature : {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
print("----------------------------------------------------------")