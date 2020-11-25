import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<network error>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<weather server is unreachable>'


def what_temperature(weather):
    if (weather == '<network error>' or
            weather == '<weather server is unreachable>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
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
        if temperature < 18:
            return 'Very cold outside'
        elif temperature in range(18, 28):
            return 'Weather is really good'
        else:
            return 'Pretty hot'
    except ValueError:
        return "Can't parse weather"

