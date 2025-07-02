# Auth Microservice

This is the authentication microservice for an E-Commerce backend project. Built using FastAPI.

---

## 🔧 Tech Stack

* Python 3.9+
* FastAPI
* Uvicorn (ASGI server)
* PassLib (for secure password hashing)
* Pydantic (with email validation)

---

## 📁 Project Structure

```
auth_service/
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   │   └── security.py
│   ├── routes/
│   │   └── auth_routes.py
│   └── schemas/
│       └── user_schema.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
# Optional: Create virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

---

## 📍 Test Endpoints

* Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Health Check: [http://127.0.0.1:8000/api/auth/health](http://127.0.0.1:8000/api/auth/health)
* Registration: [http://127.0.0.1:8000/api/auth/register](http://127.0.0.1:8000/api/auth/register)

---

## ✅ Completed Progress

**Day 1:**

* Project setup with FastAPI boilerplate
* Project structure and folder layout
* Initial README documentation

**Day 2:**

* Implemented user registration endpoint
* Added password hashing using PassLib
* Defined user schema with Pydantic email validation
* Created route handling in `auth_routes.py`

---

## 🔮 Future Features

* JWT-based login and authentication
* Role-based access control (admin vs. customer)
* Integration with product, order, and cart services
* Admin dashboard and usage analytics

### 📊 Machine Learning Module (Planned):

* Personalized product recommendations
* Customer behavior and purchase pattern analysis

---

## 🛂 Part of Larger Project

This is one of multiple microservices in a full E-Commerce Backend system. Other services include:

* Product Service (FastAPI, MongoDB)
* Cart Service
* Order Service
* Payment & Notification Services (optional)

---

## 🧐 Author

Developed by Mohit Sharma
