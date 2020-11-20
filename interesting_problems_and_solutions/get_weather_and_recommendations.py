# Small script for getting weather for your city
import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    # parameters:
    # 'M' for wind
    # 'format' used to display variable options
    # more option on the website in api section
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<Network error>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<Server is not responding, please try again later>'


def what_temperature(weather):
    if (weather == '<Network error>' or
            weather == '<Server is not responding, please try again later>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == "-" or char == ".":
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature


def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)
        if temperature <= 0:
            return 'Very cold, like really, you better stay at home.'
        elif temperature in range(1, 12):
            return 'Pretty cold, you need a warm clothes.'
        elif temperature in range(12, 18):
            return 'Kinda chilly outside.'
        elif temperature in range(18, 26):
            return 'Best condition for a small walk.'
        else:
            return 'It\'s really hot outside.'
    except ValueError:
        return "Something went wrong..."


# Enter your city as input
current_city = input()
print(what_weather(current_city))
print(what_conclusion(what_temperature(what_weather(current_city))))
