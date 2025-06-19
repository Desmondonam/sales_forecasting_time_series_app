# 📦 Pharmaceutical Sales Forecasting MVP

This project is a ready-to-run MVP for **pharmaceutical sales forecasting** using **NeuralProphet**, **FastAPI**, **Streamlit**, **PostgreSQL**, and **Docker Compose**. It supports a full-stack data pipeline from ETL to model serving and dashboard visualization.

---

## 🛠️ Tech Stack

* **NeuralProphet + PyTorch** – Time series forecasting
* **FastAPI** – Backend API
* **PostgreSQL** – Forecast result storage
* **Streamlit** – Lightweight dashboard for MVP
* **Airflow DAG** – Synthetic data generator
* **Docker Compose** – Local container orchestration
* **GitHub Actions** – CI/CD pipeline

---

## 📁 Project Structure

```
├── app/                    # FastAPI backend
│   ├── main.py             # API endpoints
│   └── model.py            # Model training & DB logic
├── airflow/
│   └── dags/
│       └── sales_etl_dag.py # Synthetic data generator
├── streamlit_app/
│   └── dashboard.py        # Streamlit dashboard
├── frontend/               # (Optional) React frontend
│   └── src/
│       └── App.jsx
├── synthetic_sales.csv     # Sample generated dataset
├── Dockerfile              # FastAPI app Docker config
├── docker-compose.yml      # Multi-service container setup
├── requirements.txt        # Python dependencies
└── .github/workflows/ci.yml # GitHub CI workflow
```

---

## 🚀 How to Run Locally

### 1. 🔧 Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
* Python 3.10+ (for running parts manually, optional)

---

### 2. 🐳 Run the App (All Services)

```bash
# Run all containers: FastAPI, Streamlit, PostgreSQL
docker-compose up --build
```

### 3. 🔄 Generate Synthetic Sales Data

This is done automatically by Airflow DAG or manually:

```bash
python airflow/dags/sales_etl_dag.py
```

This will create `synthetic_sales.csv` file.

### 4. 🧠 Train the Model

After the synthetic data is generated:

```bash
curl http://localhost:8000/train
```

This will train the model and populate the PostgreSQL `forecast` table.

### 5. 📈 View Forecast Dashboard

Open in your browser:

```
http://localhost:8501
```

---

## 📬 API Endpoints (FastAPI)

* `GET /train` – Train model & update forecast DB
* `GET /forecast` – Return 2-week forecast from DB

---

## ⚙️ Environment Variables (Handled via Compose)

These are preconfigured in `docker-compose.yml`:

```env
POSTGRES_DB=forecast_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## ✅ CI/CD (GitHub Actions)

On every push, GitHub Actions:

* Installs dependencies
* Runs a basic model training test

---

## 📊 Next Steps

* [ ] Connect production sales database
* [ ] Replace synthetic generator with real ETL
* [ ] Add authentication (e.g., OAuth2)
* [ ] React-based rich UI (optional)

---

## 👤 Author

**Desmond Onam**
MVP for Sales Forecasting – Powered by AI ✨

---

## 📄 License

MIT – Feel free to use and modify!
