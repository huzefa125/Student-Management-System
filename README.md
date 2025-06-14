# Student Management System

## Overview
This is a comprehensive Student Management System built with Django, designed to manage various aspects of student academic life, including student information, teachers, classes, fees, marks, attendance, and AI-generated reports.

## Features
- **User Authentication:** Secure login and user management.
- **Student Management:** Add, view, edit, and delete student records.
- **Teacher Management:** Keep track of teachers and their associated subjects/classes.
- **Class Management:** Organize students into classes and assign teachers.
- **Fees Management:** Record and track student fees and payment statuses.
- **Marks Management:** Enter and view student marks for various subjects and exams.
- **Attendance Management:** Mark and track student attendance.
- **AI Reports:** Generate custom reports using AI (future or current integration).

## Technologies Used
- Python
- Django
- SQLite (default database)
- Tailwind CSS (for styling, as indicated by `tailwind` and `theme` apps)

## Setup Instructions

To get this project up and running on your local machine, follow these steps:

### 1. Clone the repository
```bash
git clone <repository-url> # Replace with your actual repository URL
cd Student-Management
```

### 2. Create a virtual environment and activate it
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt # Make sure you have a requirements.txt, or create one with your dependencies
```

### 4. Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin username, email, and password.

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Access the application
Open your web browser and navigate to:
- **Dashboard:** `http://127.0.0.1:8000/dashboard/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/` (Use the superuser credentials created above)

## Usage
- Log in with your superuser account or a regular user account.
- Navigate through the dashboard to access different sections like Students, Teachers, Classes, Fees, Marks, Attendance, and AI Reports.
- Use the provided forms to add, edit, or delete records.

## Contributing
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
This project is open source and available under the [MIT License](LICENSE). # You might want to create a LICENSE file if you haven't already.
