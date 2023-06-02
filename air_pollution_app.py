import time
from mqtt_publisher import publish

import requests

API_KEY = "ee676c54c5fe72f644596aff6e086e87"
LIMIT = 3
CITY = "Belgrade"
topic = "air_pollution"

GEOCOORD_API_URL = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit={}&appid={}"

AIR_POLLUTION_API_URL = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"


def fetch_data():
    geo_url = GEOCOORD_API_URL.format(CITY, LIMIT, API_KEY)

    geo_data = requests.get(geo_url)
    lat = geo_data.json()[0]['lat']
    lon = geo_data.json()[0]['lon']
    pollution_url = AIR_POLLUTION_API_URL.format(lat, lon, API_KEY)

    pollution_data = requests.get(pollution_url).json()['list'][0]['components']

    return pollution_data


if __name__ == "__main__":
    while True:
        message = "Air pollution data for {}: {}".format(CITY, fetch_data())
        publish(topic, message)
        time.sleep(3)

