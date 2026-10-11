from scripts.extract import get_weather
from scripts.transform import transform_data
from scripts.load import load_data

CITY = "Hyderabad"

def run_pipeline():

    raw_data = get_weather(CITY)

    transformed_df = transform_data(raw_data)

    load_data(transformed_df)

if __name__ == "__main__":
    run_pipeline()