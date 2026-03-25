# 🚀 Insurance Premium Category Predictor (Backend API)

A **production-ready Machine Learning API** that predicts the **insurance premium category** based on user details like age, BMI, income, lifestyle, and city.

---

## 🧠 Tech Stack

* **Backend:** FastAPI
* **Machine Learning:** Scikit-learn
* **Language:** Python
* **Containerization:** Docker

---

## 🔍 Features

* 📊 Predicts insurance premium category (Low / Medium / High)
* ⚡ High-performance REST API using FastAPI
* 🧠 ML pipeline with preprocessing (ColumnTransformer + Pipeline)
* 🐳 Dockerized for easy deployment
* 🔄 End-to-end pipeline (Request → Model → Response)

---

## 🏗️ Project Structure

```
.
├── main.py              # FastAPI backend
├── model/               # Trained ML model
├── requirements.txt     # Dependencies
├── Dockerfile
├── README.md
```

---

## ⚙️ Run Locally (Without Docker)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/tygopal45/insurance-premium-predictor.git
cd insurance-premium-predictor
```

---

### 2️⃣ Create and activate environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run FastAPI backend

```bash
uvicorn main:app --reload
```

👉 API runs on:
`http://127.0.0.1:8000`

---

## 🐳 Run Using Docker

### 1️⃣ Build Docker image

```bash
docker build -t insurance-api .
```

---

### 2️⃣ Run container

```bash
docker run -p 8000:8000 insurance-api
```

---

### 3️⃣ Access API

Swagger Docs:
`http://localhost:8000/docs`

---

## 🔗 API Endpoint

### POST `/predict`

#### Input:

```json
{
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

---

#### Output:

```json
{
  "predicted_category": "Medium"
}
```

---

## 🧠 ML Pipeline

* Feature Engineering:

  * BMI calculation
  * Age grouping
  * Lifestyle risk scoring
  * City tier mapping

* Preprocessing:

  * OneHotEncoding for categorical features
  * Numeric features passed directly

* Model:

  * RandomForestClassifier

---

## 🎯 Future Improvements

* 🌐 Deploy on cloud (Render / AWS / HuggingFace)
* 📈 Add probability/confidence scores
* 🧾 Save prediction history
* 📊 Add monitoring & logging

---

## 👨‍💻 Author

**Gopal Jee**
