from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import random

def generate_sales_data():
    today = pd.Timestamp.today()
    dates = pd.date_range(today - pd.Timedelta(days=60), today)
    sales = [round(1000 + random.gauss(0, 50), 2) for _ in range(len(dates))]
    df = pd.DataFrame({"date": dates, "sales": sales})
    df.to_csv("/opt/airflow/dags/synthetic_sales.csv", index=False)

with DAG("pharma_sales_etl", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    etl_task = PythonOperator(
        task_id="generate_sales_data",
        python_callable=generate_sales_data
    )
