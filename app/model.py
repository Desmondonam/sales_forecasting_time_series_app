from neuralprophet import NeuralProphet
import pandas as pd
import psycopg2
import os

def train_model(csv_path="synthetic_sales.csv"):
    df = pd.read_csv(csv_path)
    df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)

    model = NeuralProphet()
    model.fit(df, freq="D")
    future = model.make_future_dataframe(df, periods=14)
    forecast = model.predict(future)

    forecast[["ds", "yhat1"]].to_csv("forecast.csv", index=False)
    save_to_postgres(forecast.tail(14))
    return forecast

def get_forecast():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT ds, yhat1 FROM forecast ORDER BY ds DESC LIMIT 14;")
        rows = cursor.fetchall()
        return [{"ds": r[0], "yhat1": float(r[1])} for r in rows]
    except Exception as e:
        return [{"error": str(e)}]


def save_to_postgres(df):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS forecast (ds DATE PRIMARY KEY, yhat1 FLOAT);")
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO forecast (ds, yhat1) VALUES (%s, %s)
            ON CONFLICT (ds) DO UPDATE SET yhat1 = EXCLUDED.yhat1;
        """, (row["ds"], row["yhat1"]))
    conn.commit()
    conn.close()