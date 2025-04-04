# Inventory Management API

## Overview
The **Inventory Management API** is a RESTful API built using Django Rest Framework (DRF) to facilitate efficient inventory tracking. It allows users to manage inventory items, view stock levels, and generate reports. Authentication is handled via JWT tokens, ensuring secure access.

## Features
- User authentication (registration, login, logout, profile management)
- CRUD operations for inventory items
- Filtering and search functionality
- Inventory level tracking (low stock, out of stock)
- Detailed reports on inventory status
- Secure API access with JWT authentication
- Pagination for large datasets

## Tech Stack
- **Backend:** Django Rest Framework (DRF)
- **Database:** PostgreSQL / SQLite (for development)
- **Authentication:** JWT (JSON Web Tokens)
- **Deployment:** Heroku / PythonAnywhere

---

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python (>=3.10)
- PostgreSQL (or SQLite for local development)
- Virtualenv

### 1. Clone the Repository
```sh
$ git clone https://github.com/yourusername/inventory_management_api.git
$ cd inventory_management_api
```

### 2. Create a Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file and add:
```
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgres://your_db_url_here
```

### 5. Run Migrations
```sh
$ python manage.py migrate
```

### 6. Create a Superuser (Admin)
```sh
$ python manage.py createsuperuser
```

### 7. Start the Server
```sh
$ python manage.py runserver
```
The API is now running at **http://127.0.0.1:8000/**

---

## API Endpoints

### **Authentication**
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and receive a JWT token |
| GET | `/api/auth/user/` | Retrieve user profile (Authenticated users only) |
| POST | `/api/auth/logout/` | Logout the user |

### **Inventory Management**
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/inventory/` | Add a new inventory item |
| GET | `/api/inventory/` | Retrieve all inventory items |
| GET | `/api/inventory/{id}/` | Retrieve details of a specific inventory item |
| PUT | `/api/inventory/{id}/` | Update an inventory item's details |
| DELETE | `/api/inventory/{id}/` | Delete an inventory item |

### **Inventory Reports**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/inventory/low-stock/` | View all low-stock items |
| GET | `/api/inventory/out-of-stock/` | View all out-of-stock items |
| GET | `/api/inventory/reports/` | Get summary statistics |

---

## Authentication & Usage
This API uses JWT for authentication. After logging in, include the token in the `Authorization` header:
```sh
Authorization: Bearer your_token_here
```

---

## Testing
Run the following command to test the API:
```sh
$ python manage.py test
```

---

## Deployment
To deploy on **Heroku** or **PythonAnywhere**, follow these steps:
1. **Set up your production database (PostgreSQL recommended).**
2. **Configure environment variables in the hosting provider.**
3. **Run migrations in the production environment:**
   ```sh
   $ python manage.py migrate
   ```
4. **Collect static files (if needed):**
   ```sh
   $ python manage.py collectstatic --noinput
   ```
5. **Restart the server to apply changes.**

---

## Contribution Guidelines
1. **Fork the Repository**
2. **Create a New Branch**
   ```sh
   $ git checkout -b feature-branch-name
   ```
3. **Commit Changes with Standard Messages**
   ```sh
   $ git commit -m "feat: Add new inventory filter"
   ```
4. **Push to Your Fork**
   ```sh
   $ git push origin feature-branch-name
   ```
5. **Create a Pull Request**

---

## License
This project is licensed under the MIT License.

---

## Author
**Precious Akachukwu Nnorom**
- GitHub: [@akolite](https://github.com/akolite)
- LinkedIn: [Precious Nnorom](https://linkedin.com/in/precious-nnorom)

For questions or support, feel free to open an issue! 🚀

