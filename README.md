# 🎓 Flask-Based Student Registration Application with CI/CD Deployment

## 📌 Project Overview

This project is a **Flask-based web application** designed to manage student registration efficiently. It replaces manual spreadsheet-based record keeping with a structured, database-driven system, eliminating data inconsistency and duplication issues.

The application allows users to:

* Register students
* Store data in a MySQL database
* View registered students
* Deploy automatically using Jenkins CI/CD pipeline

---

## 🏗️ Architecture

![Architecture](https://github.com/user-attachments/assets/f54ae136-1c82-4402-ad49-8149ead4e69a)

---

---

## 🚀 Features

### ✅ Frontend

* HTML + CSS based UI
* Student registration form
* Basic input validation

### ✅ Backend

* Flask framework
* RESTful routes
* Form handling
* Success & error messages

### ✅ Database

* MySQL integration
* Table creation for student records
* CRUD operations:

  * Create (Add student)
  * Read (View students)
  * Update (Optional)
  * Delete (Optional)

### ✅ CI/CD Pipeline

* GitHub integration
* Jenkins pipeline automation
* Automatic build & deployment

---

## 🛠️ Technologies Used

* Python (Flask)
* MySQL
* HTML, CSS
* Git & GitHub
* Jenkins
* (Optional) AWS EC2

---

## 📂 Project Structure

```
student-registration-app/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── students.html
│
├── venv/
├── app.py
├── requirements.txt
├── jenkinsfile
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/student-registration-app.git
cd student-registration-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup MySQL Database

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100)
);
```

### 5️⃣ Configure Database in `app.py`

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'student_db'
```

### 6️⃣ Run Application

```bash
python app.py
```

Visit: http://127.0.0.1:5000

---

## 🔄 Jenkins CI/CD Pipeline

### Steps:

1. Connect Jenkins with GitHub repo
2. Create Pipeline Job
3. Add `Jenkinsfile`
4. Configure:

   * GitHub webhook
   * Build trigger
5. Pipeline automatically:

   * Pulls code
   * Installs dependencies
   * Runs application / deploys

---

## 📸 Screenshots

### 🔹 Home Page

<img width="1366" height="731" alt="Screenshot (89)" src="https://github.com/user-attachments/assets/a479c53d-9c9e-4cb9-ae61-3e840502b60f" />


### 🔹 Registration Form

<img width="1366" height="735" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/04fe40e3-fc9f-4c14-afff-675c4704b872" />


### 🔹 Student List Page

<img width="1366" height="731" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/a3c6fef3-c06f-40bf-8fa2-bdae3705975d" />


### 🔹 Jenkins Pipeline

<img width="1366" height="733" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/1b732e0a-ef21-4dc6-b8d1-34214ee6ef3e" />

<img width="1366" height="731" alt="Screenshot (86)" src="https://github.com/user-attachments/assets/0e8d5b97-af64-4de4-b040-15d3e85dd647" />


---

---

## 🔮 Future Improvements

* Add user authentication (login system)
* Implement update & delete functionality
* Use REST API architecture
* Docker containerization
* Deploy on AWS EC2 with Nginx
* Improve UI with Bootstrap

---
---

## 📄 License

This project is for educational purposes.
