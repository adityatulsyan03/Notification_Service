# 📬 Flask Notification Service

A simple web-based notification management system built with Flask and Bootstrap. This app allows users to send and retrieve notifications of various types (Email, SMS, In-App).

---

## 🚀 Features

- Send notifications via a form (Email, SMS, or In-App)
- Dynamically render additional input fields based on notification type
- Fetch all notifications for a user
- Fetch a specific notification using user ID and notification ID
- In-memory storage (dictionary-based) — no external database required
- Responsive Bootstrap UI

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap 5, JavaScript (Fetch API)

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/flask-notification-service.git
cd flask-notification-service
```
2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install Flask
```
4. **Run the application**
```bash
python app.py
```
5. **Open in browser**
```bash
http://127.0.0.1:5000/
```
# 📬 API Endpoints
➕ Create a Notification
POST /notifications

Request JSON:
```bash
{
  "user_id": "123",
  "type": "email",
  "message": "Your OTP is 4567",
  "target": "user@example.com"
}
```
- Response: 201 Created
```bash
{
  "status": "success",
  "timestamp": "2025-05-17T12:00:00"
}
```
# 📋 Get All Notifications for a User
GET /users/<user_id>/notifications

Response: List of notifications

---

# 🔍 Get a Specific Notification
GET /users/<user_id>/<notification_id>/notifications

Response: Single notification or 404 error

---

# 🎨 UI Preview
The app includes a simple Bootstrap-based web interface to:

Submit new notifications

View all notifications by user

View a specific notification by ID

---

# ⚠️ Notes
Data is stored in memory (in a Python dictionary), so it will reset on server restart.

This project is for learning/demo purposes. For production, consider using a database like PostgreSQL, authentication, and rate limiting.

---

# 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

# 🙋‍♂️ Author
Your Name – @adityatulsyan03

Feel free to open issues or pull requests to improve the project.

---

Let me know if you want me to add deployment instructions (e.g., on Heroku or Render) or convert this to use a persistent database like SQLite or PostgreSQL.
