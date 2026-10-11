import json
from urllib.parse import urlencode
from urllib.request import urlopen

def get_weather(city):

    API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"

    params = urlencode({"q": city, "appid": API_KEY, "units": "metric"})
    url = f"https://api.openweathermap.org/data/2.5/weather?{params}"

    with urlopen(url) as response:
        return json.loads(response.read())