import pandas as pd
from datetime import datetime

def transform_data(data):

    transformed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather_condition": data["weather"][0]["main"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.now()
    }

    return pd.DataFrame([transformed])