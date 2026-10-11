from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine(
        "postgresql+psycopg2://postgres:admin@localhost:5432/weatherdb"
    )

    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",
        index=False
    )

    print("Data Loaded Successfully")