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

- Login page
  <img width="1504" height="531" alt="{2DC0201A-DB4F-460E-ABCF-0A2ABA0CE619}" src="https://github.com/user-attachments/assets/1303a467-87b6-48a4-a5ca-eb89c2998510" />

- Admin inventory management
  <img width="1220" height="631" alt="{6349AEFE-2010-4AA6-809C-0D23C0761D96}" src="https://github.com/user-attachments/assets/65b58730-4761-4377-8ee4-7d54e4924c25" />

- Normal user access control
  <img width="1270" height="608" alt="{69AF8A84-403C-4713-A765-0F0F84CDCD0B}" src="https://github.com/user-attachments/assets/98ab433b-3c18-4235-969a-b2703fc91f2c" />

- Input validation errors
  <img width="1189" height="565" alt="{F5E52162-E389-4235-85AD-B80741CE2780}" src="https://github.com/user-attachments/assets/18c629a2-87af-46b6-a4c0-f3d28b9cdd2b" />
  <img width="1201" height="644" alt="{A0C98D23-AB1B-4430-BCFC-384380FEC063}" src="https://github.com/user-attachments/assets/57c0a217-d9b6-4939-bf88-74bdf462b617" />

- Audit log page
  <img width="1249" height="586" alt="{FF7ED6BF-CA79-411C-8935-2DDF13E1B9D2}" src="https://github.com/user-attachments/assets/9879ce72-ec59-4edd-aa6e-397474fc4c56" />

- OWASP ZAP dynamic testing results
  <img width="1222" height="878" alt="{ACAD56F7-D8CA-41E2-9BCC-775104323A15}" src="https://github.com/user-attachments/assets/84fd0f48-2af9-4128-8dd5-b0eea4e544d7" />





