# HelpDesk API

A backend API for managing technical support tickets. This project simulates a real-world helpdesk system with authentication, role-based access control, and ticket lifecycle management.

---

## 🚀 Features

* User registration and authentication (JWT)
* Role-based access control (User, Technician, Admin)
* Ticket creation and management
* Ticket status tracking (open, in progress, closed)
* Priority levels (low, medium, high)
* Comments on tickets
* Filtering and pagination
* RESTful API design

---

## 🛠️ Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication

---

## 📂 Project Structure

```
app/
 ├── main.py
 ├── models/
 ├── schemas/
 ├── routes/
 ├── services/
 ├── database/
 └── core/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/helpdesk-api.git
cd helpdesk-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost:5432/helpdesk
SECRET_KEY=your_secret_key
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Interactive docs available at:

```
http://localhost:8000/docs
```

---

## 🔐 Authentication

This API uses JWT for authentication.

Include the token in requests:

```
Authorization: Bearer <your_token>
```

---

## 🧪 Example Endpoints

### Create Ticket

```
POST /tickets
```

### Get Tickets

```
GET /tickets
```

### Update Ticket Status

```
PATCH /tickets/{id}
```

---

## 🎯 Purpose

This project was built to demonstrate backend development skills, including:

* Designing real-world systems
* Implementing authentication and authorization
* Working with relational databases
* Structuring scalable backend applications

---

## 📌 Future Improvements

* Unit and integration tests
* Docker support
* CI/CD pipeline
* Frontend integration

---
