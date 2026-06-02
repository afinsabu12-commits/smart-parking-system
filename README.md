# Smart Parking System

## Overview

Smart Parking System is a web-based application that helps users find, book, and manage parking slots efficiently. The system provides real-time parking slot availability and simplifies parking management through a user-friendly interface.

## Features

* User Registration and Login
* Secure Authentication
* Parking Slot Management
* Real-Time Slot Availability
* Parking Slot Booking
* Booking History
* Admin Dashboard
* Role-Based Access Control
* Security Features (JWT, Password Hashing, Rate Limiting)
* Monitoring and Logging

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Backend

* Python
* Flask

### Database

* MySQL

### Cloud & DevOps

* AWS EC2
* Nginx Reverse Proxy
* Docker
* Git & GitHub
* GitHub Actions (CI/CD)
* AWS S3 (Backup Storage)
* CloudWatch Monitoring

## Security Features

* Password Hashing using bcrypt
* HTTPS/SSL Configuration
* SQL Injection Prevention
* XSS Protection
* Rate Limiting
* Security Headers
* Fail2Ban Protection

## Installation

### Clone Repository

```bash
git clone https://github.com/afinsabu12-commits/smart-parking-system.git
cd smart-parking-system
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a MySQL database and update the database credentials in the application configuration.

### Run Application

```bash
python app.py
```

Application will run at:

```text
http://localhost:5000
```

## Docker Deployment

Build Docker Image:

```bash
docker build -t smart-parking .
```

Run Container:

```bash
docker run -d -p 5000:5000 --name smart-parking-app smart-parking
```

## AWS Deployment

* Deployed on AWS EC2
* Nginx configured as Reverse Proxy
* Automated Backups using Cron Jobs
* Monitoring using CloudWatch and System Logs

## Monitoring & Logging

* System Monitoring using htop
* Application Logs using journalctl
* Fail2Ban Security Monitoring
* Health Check Endpoints
* CloudWatch Integration

## Project Structure

```text
smart-parking-system/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── static/
├── templates/
├── backups/
└── README.md
```

## Author

Afin Sabu

## License

This project is developed for educational and internship purposes.
