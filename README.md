# GraphQL ETL Mock API

A lightweight mock API designed to simulate vendor data interfaces for ETL pipelines, integration testing, and data validation workflows.

---

### Requirements
- Python 3.9+
- PostgreSQL running locally

---

## ⚡ Quick Start (2 minutes)

```bash
git clone https://github.com/your-username/graphql-etl-mock-api
cd graphql-etl-mock-api

python 00_init_env.py
pip install -r requirements.txt
uvicorn app:app --reload
```

Then run:

```bash
curl http://127.0.0.1:8000/
```

---

## 📦 Example Request

```bash
curl -X POST http://127.0.0.1:8000/graphql \
-H "Content-Type: application/json" \
-d '{"operation":"exchanges","variables":{"limit":5,"offset":0}}'
```

---

## 📊 Example Output

```json
{
  "exchange": "ASX",
  "company_count": 500
}
```

---

## 🧩 Overview

This project exposes a simplified GraphQL-style contract over relational data stored in PostgreSQL.

It is designed as a reusable demo environment for:

- ETL and ingestion workflows  
- API integration testing  
- Vendor API simulation  
- Relational → domain object mapping  
- TestOps / data validation scenarios  

Instead of implementing a full GraphQL server, this uses a lightweight operation dispatcher to simulate GraphQL-style queries while keeping the system simple and controllable.

---

## ⚙️ Core Operations

### 1. `exchanges`
Returns available exchanges and company counts.

### 2. `companies(exchange, limit, offset)`
Returns companies filtered by exchange.

### 3. `company(id)`
Returns a full company payload including:

- Base attributes  
- Grouped fundamentals  
- Owners  
- Insider transactions  

---

## 🏗️ Architecture

Client → FastAPI → db.py → PostgreSQL → mappers.py

---

## 📁 Repository Structure

```
graphql-etl-mock-api/
├─ 00_init_env.py
├─ app.py
├─ db.py
├─ mappers.py
├─ queries.py
├─ requirements.txt
├─ .env.example
├─ README.md
```

---

## 🚀 Setup (Detailed)

### Requirements

- Python 3.9+
- PostgreSQL running locally

---

### 1. Initialize environment

```bash
python 00_init_env.py
```

This will create a `.env` file.

---

### 2. Configure database connection

Open the `.env` file and update with your PostgreSQL credentials:

```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run API

```bash
uvicorn app:app --reload
```

---

### 5. Verify API is running

```bash
curl http://127.0.0.1:8000/
```

If successful, the API will return a response confirming it is running.

---

## 🧠 Why This Matters

- Simulates real vendor API dependencies without external services  
- Enables controlled ETL testing environments  
- Supports validation and failure isolation  
- Demonstrates API → DB → domain object mapping patterns  
- Provides a reproducible TestOps / data validation environment  

---

## 📍 Current State

**MVP v1 – Frozen**

- ✔ Ready for demo  
- ✔ Reproducible locally  
- ✔ Covers core ETL + API testing scenarios  

---

## 🔮 Future Enhancements

- Failure injection  
- Retry / backoff simulation  
- Pagination metadata  
- ETL consumer examples  

---

## ⚠️ Notes

This is a mock API for testing and demonstration purposes only.  
Not intended for production use.

---

## 🎯 Summary

This project demonstrates how to simulate external data dependencies, enabling reliable testing of ETL pipelines, integrations, and data validation workflows without relying on real vendor APIs.
