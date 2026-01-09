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

##  Features

###  Authentication & Authorization
- User login and logout
- User registration for normal users
- Role-based access control:
  - **Admin**: Full access (CRUD + Audit Log)
  - **Normal User**: View-only access

###  Inventory Management
- Add, edit, delete products (Admin only)
- View product list
- Search products by name
- Pagination for product listing

###  Audit Logging
- Logs all critical actions:
  - Product added
  - Product edited
  - Product deleted
- Records:
  - Username
  - Action performed
  - Product name
  - Timestamp
- Audit log accessible **only by admin**

###  Security Enhancements
- CSRF protection on all forms
- Input validation (quantity, price, password)
- Django ORM to prevent SQL Injection
- Automatic password hashing
- Secure session management

###  User Interface Improvements
- Clean and professional navigation header
- Auto-dismiss user feedback messages
- Confirmation dialog for delete actions
- Responsive and readable layout


