import requests

from datetime import datetime

api_key = '7d0bee86bd92f39b064df3f008a5f20e'
location = input("enter the city name: ")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=7d0bee86bd92f39b064df3f008a5f20e"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-----------------------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))
print("-----------------------------------------------------------")

print("current tempareture is: {:.2f} deg C".format(temp_city))
print("current weather desc :", weather_desc)
print("current Humidity     :", hmdt, '%')
print("current wind speed :", wind_spd, 'kmph')
