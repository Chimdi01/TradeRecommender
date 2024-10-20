import requests
import datetime
import calendar


def output_details_current(response):
    if response.status_code == 200:
        data = response.json()
        print("*"*30)
        print(data)
        print("*" * 30)
        temp = data['current']['temp']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_speed']
        precipitation = data['hourly'][0]['pop']
        desc = data['current']['weather'][0]['description']
        print(f'Temperature: {temp} C')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')

def output_details_historical_one_day(response):
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("*"*30)
        print(data)
        print("*" * 30)
        temp = data['data'][0]['temp']
        wind_speed = data['data'][0]['wind_speed']
        humidity = data['data'][0]['humidity']
        pressure = data['data'][0]['pressure']
        pressure = data['data'][0]['pressure']
        # temp_max = data['temperature']['max']
        desc = data['data'][0]['weather'][0]['description']
        print(f'Temperature: {temp} C')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')

def output_details_historical_aggregate(response):
    if response.status_code == 200:
        data = response.json()
        print("*"*30)
        print(data)
        print("*" * 30)
        temp_min = data['temperature']['min']
        temp_max = data['temperature']['max']
        desc = data['data']['weather'][0]['description']
        print(f'Temperature: {(temp_max + temp_min)/2} C')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')

def output_details_future_details(response):
    if response.status_code == 200:
        data = response.json()
        print("*"*30)
        print(data)
        print("*" * 30)
        temp = data['data'][0]['temp']
        # temp_max = data['temperature']['max']
        desc = data['data'][0]['weather'][0]['description']
        print(f'Temperature: {temp} C')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')

def return_requested_values(call_type):
    api_key = 'fcb27af38e997e0eff7b44aeabfb15f9'
    one_key = '738e2e1195001ea36f41963526e34233'
    lat = '33.44'
    lon = '-94.04'
    dt = date_to_unix_time('15-02-2022')
    date = '15-02-2022'
    date_historic = date_to_unix_time('15-02-1987')
    tz = '+03:00'

    if (call_type == 'current_details'):
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={one_key}'
        output_details_current(requests.get(url))

    if (call_type == 'historical_details_one_day'):
        # url = (f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}'
        #  f'&units=metric&dt={date_historic}appid={one_key}')
        url = (f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}'
               f'&dt={date_historic}&units=metric&appid={api_key}')
        output_details_historical_one_day(requests.get(url))

    if (call_type == 'historical_details_aggregate'):
        url = ( f'https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}'
         f'&date={date}&tz={tz}&units=metric&appid={one_key}')
        output_details_historical_aggregate(requests.get(url))

    if (call_type == 'future_details'):
        url = (f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}'
               f'&dt={dt}&units=metric&appid={api_key}')
        output_details_future_details(requests.get(url))


def convert_kelvin(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    return celsius, fahrenheit


def date_to_unix_time(date_str):
    # Parse the input date string into a datetime object
    date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
    # Convert the datetime object to a Unix timestamp
    unix_time = str(calendar.timegm(date_obj.utctimetuple()))
    return unix_time
