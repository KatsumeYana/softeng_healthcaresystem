# 🏥 St. Blaise Medical Clinic & Pharmacy# St. Blaise Medical Clinic & Pharmacy# Healthcare Management System# Healthcare Management System# Healthcare Management System Backend# St. Blaise Medical Clinic & Pharmacy - Backend API



A complete healthcare management system with Flutter frontend and FastAPI backend.



## 🚀 Super Quick StartA complete healthcare management system with Flutter frontend and FastAPI backend.



**Just double-click:** `start-all-test.bat`



This automated script will:## 🚀 Quick StartA simple healthcare management system with Flutter frontend and FastAPI backend.

- ✅ Initialize SQLite database with admin user

- ✅ Start FastAPI backend server (port 8000)

- ✅ Test admin login (admin/admin123)

- ✅ Verify database create/read operations### Prerequisites

- ✅ Launch Flutter frontend (port 3000)

- ✅ Confirm everything is working- Docker Desktop (recommended)



## 🎯 Alternative Starts- OR Python 3.11+ and Flutter SDK## 🚀 Quick StartA complete full-stack healthcare management system with Flutter frontend, FastAPI backend, and MySQL database.



### Option 1: Interactive Menu

Double-click: `start.bat` for a menu with options

### Option 1: Run with Docker (Recommended)

### Option 2: Manual Commands

```powershell

# Backend only

cd backend```powershell### Backend

python init_db.py

python main.py# Start the backend



# Frontend only (new terminal)docker compose up -d backend```bash

cd frontend

flutter run -d chrome --web-port 3000



# Connection test only# Access the APIcd backend## 🏗️ Project StructureA FastAPI-based backend for healthcare management with patient records, appointments, and drug management.This repository contains the complete backend source code for the St. Blaise Medical Clinic & Pharmacy management system. It is built with Python using the FastAPI framework and connects to a MySQL database.

cd frontend

flutter run -d chrome lib/connection_test.dart# http://localhost:8000/docs

```

```python -m uvicorn main:app --reload

### Option 3: Docker (if installed)

```powershell

docker compose up -d backend

```### Option 2: Run Manually```



## 🌐 Access Points



- **Frontend App**: http://localhost:3000**Backend:**

- **Backend API Docs**: http://localhost:8000/docs

- **Backend Health**: http://localhost:8000```powershell



## 🔐 Login Credentialscd backend### Frontend```



- **Username**: `admin`pip install -r requirements.txt

- **Password**: `admin123`

python init_db.py```bash

## 📋 What Gets Tested Automatically

python main.py

The `start-all-test.bat` script verifies:

```cd frontendhealthcare_system/

1. **Database Setup** - SQLite database created and initialized

2. **Backend Health** - FastAPI server responds on port 8000

3. **Authentication** - Admin login works with correct credentials

4. **Database Write** - Can create new patient records**Frontend:**flutter run -d chrome --web-port 3000

5. **Database Read** - Can retrieve patient list

6. **Frontend Launch** - Flutter app starts successfully```powershell



## 📁 Project Structurecd frontend```├── 📁 frontend/              # Flutter web application## Quick StartThis backend provides a robust, secure, and scalable foundation for the Flutter frontend application, implementing all required forms and features as specified in the project documentation.



```flutter pub get

├── 📁 backend/              # FastAPI Python backend

│   ├── main.py             # API server entry pointflutter run -d chrome --web-port 3000

│   ├── init_db.py          # Database initialization

│   ├── Dockerfile          # Docker container config```

│   └── requirements.txt    # Python dependencies

├── 📁 frontend/            # Flutter web application## 🌐 Access Points│   ├── lib/                  # Flutter source code

│   ├── lib/main.dart       # Main Flutter app

│   └── lib/connection_test.dart # Connection testing## 🌐 Access Points

├── start-all-test.bat      # Automated full system test

├── start.bat               # Interactive startup menu

└── docker-compose.yml      # Docker configuration

```- **Frontend App**: http://localhost:3000



## 🛠️ Features Tested- **Backend API**: http://localhost:8000/docs- **Backend API**: http://localhost:8000/docs│   ├── web/                  # Web-specific files



- **Patient Management**: Create, read, update patient records- **API Health**: http://localhost:8000

- **User Authentication**: JWT-based login system

- **Database Operations**: SQLite CRUD operations- **Frontend App**: http://localhost:3000

- **API Endpoints**: RESTful API with FastAPI

- **Frontend-Backend Communication**: HTTP requests with CORS## 🔒 Login Credentials

- **Error Handling**: Connection and authentication error handling

│   ├── pubspec.yaml          # Flutter dependencies

## 🔧 Troubleshooting

- Username: `admin`

If the automated test fails:

- Password: `admin123`## 📁 Project Structure

1. **Python not found**: Install Python 3.11+

2. **Flutter not found**: Install Flutter SDK

3. **Port 8000 busy**: Close other applications using port 8000

4. **Database errors**: Delete `backend/healthcare.db` and restart## 📁 Project Structure│   └── README.md             # Frontend documentation### Prerequisites---

5. **Dependencies missing**: Run `pip install -r backend/requirements.txt`



## 🎉 Success Indicators

``````

When everything works, you'll see:

- ✅ Green checkmarks in the console├── 📁 backend/               # FastAPI Python backend

- ✅ Backend accessible at http://localhost:8000/docs

- ✅ Frontend opens in Chrome browser│   ├── main.py              # API entry point├── 📁 backend/          # FastAPI Python server├── 📁 backend/               # FastAPI Python backend

- ✅ Login screen accepts admin/admin123

- ✅ Patient data saves and loads correctly│   ├── Dockerfile           # Docker container config



**Ready to go!** 🚀│   ├── requirements.txt     # Python dependencies│   ├── main.py         # API entry point

│   ├── init_db.py           # Database setup

│   ├── models/              # Database models│   ├── models/         # Database models│   ├── main.py               # FastAPI application- Python 3.8+ installed

│   ├── routes/              # API endpoints

│   ├── utils/               # Utilities│   └── routes/         # API endpoints

│   └── config/              # Configuration

├── 📁 frontend/             # Flutter web app├── 📁 frontend/        # Flutter web app│   ├── models/               # Database models

│   ├── lib/                 # Flutter source code

│   └── pubspec.yaml         # Flutter dependencies│   └── lib/           # Flutter source code

├── docker-compose.yml       # Docker services

└── README.md               # This file└── 📁 database/        # MySQL setup│   ├── routes/               # API endpoints- Virtual environment already set up## Features Implemented

```

    └── schema.sql     # Database schema

## 🛠️ Development

```│   ├── utils/                # Utility functions

### Stop Services

```powershell

# Docker

docker compose down## 🔧 One-Time Setup│   ├── config/               # Configuration



# Manual (Ctrl+C in terminals)

```

### 1. Install Python Dependencies│   ├── venv/                 # Virtual environment

### View Logs

```powershell```bash

docker compose logs -f backend

```pip install fastapi uvicorn sqlalchemy pymysql cryptography python-jose passlib python-multipart pydantic pydantic-settings python-dotenv│   ├── requirements.txt      # Python dependencies### Run the Backend- **Modern API Framework**: Built with **FastAPI** for high performance, automatic data validation, and interactive API documentation.



### Database Management```

The SQLite database is automatically created and seeded with an admin user when you run `init_db.py` or start the Docker container.

│   └── .env                  # Environment variables

## 🔧 Features

### 2. Install Flutter Dependencies

- **Patient Management**: Add, view, update patient records

- **Drug Inventory**: Manage pharmacy stock and prescriptions  ```bash├── 📁 database/              # Database setup and schema- **Relational Database**: Uses **MySQL** for structured and reliable data storage, managed with **SQLAlchemy ORM**.

- **User Authentication**: JWT-based secure login

- **Role-Based Access**: Admin, Doctor, Pharmacist, Assistant rolescd frontend && flutter pub get

- **Search & Filter**: Find patients and drugs quickly

- **REST API**: Full CRUD operations via FastAPI```│   ├── schema.sql            # MySQL database schema

- **Modern UI**: Material Design 3 Flutter interface


### 3. Setup Database (Optional)│   └── README.md             # Database setup guide**Option 1: Double-click the run.bat file**- **Full CRUD Operations**: Provides complete Create, Read, Update, and Delete functionality for patients and drugs.

```bash

mysql -u root -p < database/schema.sql├── 🚀 start-all.bat          # Start both frontend and backend

```

├── 🚀 start-backend.bat      # Start backend only- Simply double-click `run.bat` in the project folder- **Authentication & Security**: Implements **JWT (JSON Web Tokens)** for secure, token-based authentication and password hashing using `bcrypt`.

## 🔒 Login Credentials

- Username: `admin`├── 🚀 start-frontend.bat     # Start frontend only

- Password: `admin123`

└── 📄 README.md              # This file- **Role-Based Authorization**: Endpoints are protected based on user roles (Admin, Doctor, Pharmacist, Assistant/Cashier), ensuring users can only perform actions they are permitted to.

## 🛑 Stop Applications

Press `Ctrl + C` in the terminals running the applications.```

**Option 2: Command line**- **Data Validation**: Leverages **Pydantic** for rigorous request and response data validation, preventing invalid data from entering the system.

## 🚀 Quick Start

```bash- **Dependency Injection**: Uses FastAPI's dependency injection system for clean, reusable code (e.g., database sessions, user authentication).

### Option 1: Start Everything (Recommended)

```bash# Open PowerShell/Command Prompt in project folder- **CORS Enabled**: Configured with CORS middleware to allow seamless communication with the Flutter frontend.

# Double-click or run:

start-all.batrun.bat

```

This will start both backend and frontend automatically.```### Forms Implemented



### Option 2: Start Individually

```bash

# Start backend only**Option 3: Manual start**This backend successfully implements all four required forms:

start-backend.bat

```bash

# Start frontend only (in another terminal)

start-frontend.bat# Activate virtual environment and start server| Form Type | Form Name | Endpoint | Description |

```

venv\Scripts\activate|---|---|---|---|

## 🌐 Access Points

python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload| **Major Form** | Add New Patient | `POST /patients` | A comprehensive form with over 15 fields for registering a new patient. | 

After starting the applications:

- **Frontend**: http://localhost:3000```| **Major Form** | Add New Drug | `POST /drugs` | A form with 10 fields for adding a new drug to the system formulary. |

- **Backend API**: http://localhost:8000/docs

- **API Health**: http://localhost:8000/| **Supporting Form** | Login Form | `POST /auth/token` | Secure user login with username and password, returning a JWT token. |



## 📋 Prerequisites### Access the API| **Supporting Form** | Search Records | `GET /search/...` | Flexible search endpoints for finding patients and drugs by various criteria. |



### Backend Requirements- **API Documentation**: http://localhost:8000/docs

- Python 3.8+

- Virtual environment (included)- **Health Check**: http://localhost:8000/---

- All dependencies in requirements.txt

- **Alternative Docs**: http://localhost:8000/redoc

### Frontend Requirements

- Flutter SDK 3.0+## Project Structure

- Chrome browser (for web development)

### Stop the Server

### Database Requirements

- MySQL Server 8.0+Press `Ctrl + C` in the terminalThe project is organized into a modular and scalable structure:

- Database setup (see database/README.md)



## 🔧 Manual Setup

## API Endpoints```

### 1. Database Setup

```bash/home/ubuntu/st_blaise_backend/

cd database

# Follow instructions in database/README.md### Authentication├── config/                 # Configuration files (database, settings)

mysql -u root -p < schema.sql

```- `POST /auth/login` - User login│   ├── __init__.py



### 2. Backend Setup- `POST /auth/register` - User registration│   ├── database.py         # SQLAlchemy engine and session management

```bash

cd backend│   └── settings.py         # Pydantic settings management (loads .env)

# Virtual environment already configured

venv\Scripts\activate### Patients├── models/                 # SQLAlchemy database models (tables)

pip install -r requirements.txt

python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload- `GET /patients/` - List all patients│   ├── __init__.py

```

- `POST /patients/` - Create new patient│   ├── drug.py

### 3. Frontend Setup

```bash- `GET /patients/{id}` - Get patient by ID│   ├── patient.py

cd frontend

flutter pub get- `PUT /patients/{id}` - Update patient│   └── user.py

flutter run -d chrome --web-port 3000

```- `DELETE /patients/{id}` - Delete patient├── routes/                 # FastAPI API routers (endpoints)



## 🔌 Testing Backend-Frontend Connection│   ├── __init__.py



### 1. Start Backend### Drugs│   ├── auth.py             # Login endpoint

```bash

start-backend.bat- `GET /drugs/` - List all drugs│   ├── drugs.py            # Drug management endpoints

```

Verify at: http://localhost:8000/docs- `POST /drugs/` - Add new drug│   ├── patients.py         # Patient management endpoints



### 2. Start Frontend- `GET /drugs/{id}` - Get drug by ID│   └── search.py           # Search endpoints

```bash

start-frontend.bat- `PUT /drugs/{id}` - Update drug├── utils/                  # Utility functions and schemas

```

Access at: http://localhost:3000- `DELETE /drugs/{id}` - Delete drug│   ├── __init__.py



### 3. Test Connection│   ├── schemas.py          # Pydantic validation schemas

- Login to frontend application

- Check browser developer tools for API calls### Appointments│   └── security.py         # Password hashing, JWT, authorization

- Verify API responses in backend logs

- `GET /appointments/` - List appointments├── .env                    # Environment variables (local development)

## 🏥 Features

- `POST /appointments/` - Create appointment├── .env.example            # Example environment file

### Frontend (Flutter Web)

- ✅ Responsive design (mobile, tablet, desktop)- `GET /appointments/{id}` - Get appointment by ID├── .gitignore              # Files to ignore in version control

- ✅ Patient management interface

- ✅ Appointment scheduling- `PUT /appointments/{id}` - Update appointment├── init_db.py              # Script to create tables and seed data

- ✅ Drug inventory management

- ✅ User authentication- `DELETE /appointments/{id}` - Delete appointment├── main.py                 # Main FastAPI application entry point

- ✅ PWA support

├── README.md               # This file

### Backend (FastAPI)

- ✅ RESTful API endpoints## Project Structure├── requirements.txt        # Python dependencies

- ✅ JWT authentication

- ✅ Database integration```├── run.sh                  # Script to start the development server

- ✅ API documentation (Swagger)

- ✅ CORS enabled├── main.py              # FastAPI application entry point└── setup.sh                # Script for initial project setup

- ✅ Data validation

├── requirements.txt     # Python dependencies```

### Database (MySQL)

- ✅ Normalized schema├── run.bat             # Quick start script

- ✅ Patient records

- ✅ Drug inventory├── models/             # Database models---

- ✅ Appointment management

- ✅ User authentication├── routes/             # API route definitions

- ✅ Sample data included

├── utils/              # Utility functions## Setup and Installation

## 🛠️ Development

├── config/             # Configuration files

### Backend Development

```bash└── venv/               # Virtual environmentFollow these steps to set up and run the backend server.

cd backend

venv\Scripts\activate```

# Make changes to Python files### Prerequisites

# Server auto-reloads on file changes

```1.  **Python 3.11** or higher.

2.  **MySQL Server**: Ensure you have a running MySQL instance.

### Frontend Development

```bash### Step 1: Clone the Repository

cd frontend

# Make changes to Flutter filesFirst, get the code. If this were a Git repository, you would run:

# Hot reload available with 'r' in terminal

``````sh

# git clone <repository_url>

## 🔒 Default Credentials# cd st_blaise_backend

- Username: `admin````

- Password: `admin123`

- Role: `admin`### Step 2: Configure Environment Variables



## 📞 API EndpointsCreate a `.env` file by copying the example file:



### Authentication```sh

- `POST /auth/login` - User logincp .env.example .env

- `POST /auth/register` - User registration```



### PatientsNow, edit the `.env` file and update the `DATABASE_PASSWORD` and other settings to match your local MySQL configuration.

- `GET /patients/` - List patients

- `POST /patients/` - Create patient```dotenv

- `GET /patients/{id}` - Get patient# .env

- `PUT /patients/{id}` - Update patientDATABASE_HOST=localhost

- `DELETE /patients/{id}` - Delete patientDATABASE_PORT=3306

DATABASE_USER=root

### DrugsDATABASE_PASSWORD=your_mysql_password # <-- CHANGE THIS

- `GET /drugs/` - List drugsDATABASE_NAME=st_blaise_clinic

- `POST /drugs/` - Add drug

- `GET /drugs/{id}` - Get drugSECRET_KEY=a-very-secret-key-that-you-should-change

- `PUT /drugs/{id}` - Update drug# ... other settings

- `DELETE /drugs/{id}` - Delete drug```



### Appointments### Step 3: Create the MySQL Database

- `GET /appointments/` - List appointments

- `POST /appointments/` - Create appointmentConnect to your MySQL server and create the database specified in your `.env` file.

- `GET /appointments/{id}` - Get appointment

- `PUT /appointments/{id}` - Update appointment```sql

- `DELETE /appointments/{id}` - Delete appointment-- Example MySQL command

CREATE DATABASE st_blaise_clinic;

## 🛑 Stopping the Applications```



- **Backend**: Press `Ctrl + C` in backend terminal### Step 4: Run the Setup Script

- **Frontend**: Press `Ctrl + C` in frontend terminal

- **Both**: Close the terminal windowsMake the setup script executable and run it. This will create a Python virtual environment, install all dependencies, and initialize the database.



## 🐛 Troubleshooting```sh

chmod +x setup.sh

### Backend Issues./setup.sh

- Check Python version: `python --version````

- Verify virtual environment: `venv\Scripts\activate`

- Check dependencies: `pip list`The script will prompt you to initialize the database. Type `y` and press Enter. This will create all the necessary tables and seed them with initial user and drug data.



### Frontend Issues---

- Check Flutter: `flutter doctor`

- Clear cache: `flutter clean && flutter pub get`## Running the Server

- Check Chrome: Ensure Chrome is installed

To start the development server, simply run the `run.sh` script:

### Database Issues

- Verify MySQL service is running```sh

- Check connection string in backend/.env./run.sh

- Ensure database exists: `SHOW DATABASES;````



## 📁 Next StepsThe API will be available at `http://localhost:8000`.



1. **Database**: Set up MySQL and run schema.sql## API Documentation

2. **Backend**: Test API endpoints at /docs

3. **Frontend**: Customize UI and componentsOnce the server is running, you can access the interactive API documentation in your browser:

4. **Integration**: Test full-stack functionality
-   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
-   **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces allow you to explore and test all API endpoints directly from your browser.

---

## Initial Login Credentials

The database is seeded with four initial users, each with a different role. You can use these to test the API's authorization features.

| Role | Username | Password |
|---|---|---|
| Admin | `admin_mark` | `admin123` |
| Doctor | `dr_anasantos` | `doctor123` |
| Pharmacist | `pharm_isabella` | `pharm123` |
| Assistant/Cashier | `asst_juan` | `assistant123` |

### How to Authenticate

1.  Go to the `/docs` page.
2.  Navigate to the `POST /auth/token` endpoint.
3.  Click "Try it out" and enter the username and password for one of the users above.
4.  Execute the request. You will receive an `access_token`.
5.  Click the "Authorize" button at the top of the page, and enter `Bearer <your_token>` (e.g., `Bearer eyJhbGciOi...`).
6.  You can now access the protected endpoints!
