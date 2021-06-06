from flask import current_app
import requests 

def weather_by_city(lat, lon):

    weather_url = current_app.config["WEATHER_URL"]
    params = {
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'lang': 'ru',
        'exclude': 'minutely',
        'appid': current_app.config["WEATHER_API_KEY"]
    }
    try:
        result = requests.get(weather_url, params = params)
        result.raise_for_status()
        weather = result.json()

        if 'current' in weather:
            try:
                return weather['current']
            except (IndexError, TypeError):
                return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


    return False

if __name__ == '__main__':
    print(weather_by_city('55.89','37.47'))