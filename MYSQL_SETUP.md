# MySQL Setup Guide for Healthcare System

## Quick MySQL Installation Options

### Option 1: XAMPP (Recommended for Development)
1. Download XAMPP from: https://www.apachefriends.org/
2. Install XAMPP
3. Start XAMPP Control Panel
4. Start MySQL service
5. MySQL will be available on port 3306

### Option 2: MySQL Server Direct Install
1. Download MySQL Community Server: https://dev.mysql.com/downloads/mysql/
2. Run installer and follow setup wizard
3. Set root password (or leave blank for development)
4. Start MySQL service

### Option 3: MySQL with Docker
```bash
docker run --name mysql-healthcare -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=healthcare_system -p 3306:3306 -d mysql:8.0
```

## Setup Healthcare Database

Once MySQL is running, execute the setup script:

```bash
cd backend
python setup_mysql.py
```

The script will:
- ✅ Install required packages (pymysql, cryptography)
- ✅ Create healthcare_system database
- ✅ Create healthcare_user with password
- ✅ Create all tables (users, patients, drugs)
- ✅ Populate with sample data

## Database Connection Info

- **Host:** localhost
- **Port:** 3306
- **Database:** healthcare_system
- **Username:** healthcare_user
- **Password:** healthcare_pass

## Troubleshooting

### MySQL Connection Error
- Make sure MySQL service is running
- Check if port 3306 is available
- Verify MySQL root credentials

### Permission Denied
- Run script as administrator
- Check MySQL user permissions

### Package Installation Issues
```bash
pip install --upgrade pip
pip install pymysql cryptography
```

## Test Connection

After setup, test the backend:
```bash
cd backend
python main.py
```

Visit: http://localhost:8000/docs
- Should show API documentation
- Database endpoints should work

## Login Credentials

- **Admin:** admin / admin123
- **Doctor:** doctor / doctor123
- **Pharmacist:** pharmacist / pharm123