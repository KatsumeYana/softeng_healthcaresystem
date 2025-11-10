# St. Blaise Medical Clinic & Pharmacy

A complete healthcare information system with Flutter frontend and Python in FastAPI backend.

## Quick Start

**Just run:** `start-system.bat` 

This will automatically:
- Start the FastAPI backend server (port 8000)
- Launch the Flutter frontend (port 3000)
- Open your browser to the application

## Access Points

- **Frontend App**: http://localhost:3000
- **Backend API**: http://localhost:8000/docs
- **API Health**: http://localhost:8000

## Login Credentials

- **Username**: `admin`
- **Password**: `admin123`

## Project Structure

```
├── backend/              # FastAPI Python backend
│   ├── main.py             # API server entry point
│   ├── init_db.py          # Database initialization
│   ├── models/             # Database models
│   ├── routes/             # API endpoints
│   ├── utils/              # Utility functions
│   └── config/             # Configuration
├── frontend/            # Flutter web application
│   ├── lib/                # Flutter source code
│   └── pubspec.yaml        # Flutter dependencies
└── start-system.bat        # Quick start script
```

## Features

- **Patient Management**: Add, view, update patient records
- **Drug Inventory**: Manage pharmacy stock and prescriptions
- **User Authentication**: JWT-based secure login
- **Real-time Updates**: Automatic data synchronization
- **Connection Monitoring**: Auto-logout on server disconnect

## Prerequisites

- Python 3.11+
- Flutter SDK 3.0+
- MySQL Server 8.0+
- Chrome browser

## API Endpoints

### Authentication
- `POST /auth/token` - User login

### Patients
- `GET /patients/` - List all patients
- `POST /patients/` - Create new patient
- `GET /patients/{id}` - Get patient by ID

### Drugs
- `GET /drugs/` - List all drugs
- `POST /drugs/` - Add new drug
- `GET /drugs/{id}` - Get drug by ID

## Stopping the Applications

- Press `Ctrl + C` in the terminal windows
- Or close the terminal windows

## Troubleshooting

### Backend Issues
- Check Python version: `python --version`
- Verify dependencies: `pip install -r backend/requirements.txt`

### Frontend Issues
- Check Flutter: `flutter doctor`
- Clear cache: `flutter clean && flutter pub get`

### Database Issues
- Verify MySQL service is running
- Check connection in `backend/.env`
- Run: `python backend/init_db.py`
