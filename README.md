# FastAPI Task Management REST API

This repository contains a complete **FastAPI-based RESTful API** for a simple **Task Management system** with full CRUD, JWT authentication, SQLite database integration, input validation, filtering, and Docker deployment.

---

## 🚀 Features

- User authentication (JWT-based login & registration)
- CRUD operations for Tasks:
  - Create a new task
  - Read/list tasks
  - Update an existing task
  - Delete a task
- SQLite database integration (easy to switch to PostgreSQL/MySQL)
- Input validation with Pydantic
- Filtering and search support
- Interactive API documentation (Swagger UI & ReDoc)
- Docker deployment ready

---

## 🛠️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Database:** SQLite (via [SQLModel](https://sqlmodel.tiangolo.com/))  
- **Auth:** JWT (JSON Web Tokens)  
- **Password Hashing:** Passlib (bcrypt)  
- **Containerization:** Docker (optional)

---

## 📂 Project Structurefastapi-task-api/
│── app/
│ ├── main.py # Entry point
│ ├── models.py # Database models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # CRUD operations
│ └── auth.py # Authentication
│── .venv/ # Virtual environment (not uploaded)
│── requirements.txt # Project dependencies
│── Dockerfile # Docker setup (optional)
│── README.md # Project documentation

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-task-api.git
cd fastapi-task-api
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
API Documentation

Once the server is running, open in your browser:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🔐 Example Endpoints

Register User → POST /register

Login User → POST /login

Create Task → POST /tasks

List Tasks → GET /tasks

Update Task → PUT /tasks/{task_id}

Delete Task → DELETE /tasks/{task_id}

🐳 Docker Setup (Optional)
docker build -t fastapi-task-api .
docker run -d -p 8000:8000 fastapi-task-api

✅ Deliverables

GitHub repository with complete code

API documentation (Swagger / ReDoc)

CRUD operations + Authentication

Database integration

(Optional) Docker deployment
Added README.md with project details


# FastAPI Task Management REST API
"Update README.md with project details"

This repository contains a complete FastAPI-based RESTful API for a simple Task Management system with full CRUD, basic JWT authentication, SQLite database integration, input validation, filtering, and Docker deployment.
