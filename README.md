#  Secure Inventory System

Secure Inventory System is a Django-based web application developed for academic purposes.  
The system allows administrators to manage computer inventory securely while normal users can view available products.  
It implements authentication, role-based access control, audit logging, and multiple usability and security enhancements.

---

##  Project Information

- **Project Type**: Secure Software Development Assignment  
- **Framework**: Django  
- **Database**: SQLite3  
- **Authentication**: Django Authentication System  
- **Access Control**: Role-Based (Admin & Normal User)

---

##  Installation Steps

Follow the steps below to set up the project locally.

### Step 1: Clone the Repository
```bash
git clone https://github.com/Aidilv/secure-inventory.git
cd secure-inventory
```
### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 3. Security Features Summary

The Secure Inventory System includes the following security features:

- Secure authentication using Django authentication framework
- Role-Based Access Control (RBAC) for admin and normal users
- Server-side input validation for all critical inputs
- Protection against SQL Injection using Django ORM
- CSRF protection enabled on all forms
- Automatic password hashing
- Audit logging for administrative actions
- Django template auto-escaping to prevent XSS attacks

---

### 4. How to Run the Application

### Step 1: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 2: Create Admin User
```bash
python manage.py createsuperuser
```

### Step 3: Start the Server
```bash
python manage.py runserver
```

### Step 4: Open in Browser
```bash
http://127.0.0.1:8000/login/
```

---

### 5. Dependencies

The main dependencies used in this project include:
- Python 3.x
- Django
- SQLite3 (default Django database)
All required packages are listed in the requirements.txt file.

---

### 6. Screenshots of the System

Screenshots demonstrating system functionality and security testing are included in the project report, including:

- Login page
- Admin inventory management
- Normal user access control
- Input validation errors
- Audit log page
- OWASP ZAP dynamic testing results




