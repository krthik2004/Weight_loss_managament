Weight Loss Management System

This project is a Weight Loss Management System built using Python Django. The system helps users track their weight loss journey by adding, updating, and deleting weight entries.

🚀 Features

User registration and login

Add, edit, and delete weight records

View weight loss progress over time

Secure user authentication

🛠️ Tech Stack

Backend: Python Django

Frontend: HTML, CSS, JavaScript

Database: MySQL

⚙️ Installation Guide

Clone the Repository

git clone https://github.com/krthik2004/weightloss-management-system.git

Navigate to the Project Directory

cd weightloss-management-system

Install Dependencies

pip install -r requirements.txt

Apply Migrations

python manage.py makemigrations
python manage.py migrate

Create Superuser

python manage.py createsuperuser

Run the Development Server

python manage.py runserver

Access the Application

Visit: http://127.0.0.1:8000/

🧩 Usage

Register a new user account.

Log in to access the dashboard.

Add new weight entries with date and weight.

Edit or delete existing entries.

Track progress using the visual representation.

🗂️ Project Structure

weightloss-management-system/
    ├── weight/
    │   ├── migrations/
    │   ├── templates/
    │   ├── views.py
    │   ├── models.py
    │   └── urls.py
    ├── weightloss_management_system/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    └── requirements.txt

🛠️ API Endpoints

/api/weights/ - List and create weight entries

/api/weights/<id>/ - Retrieve, update, and delete entries

🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

🧑‍💻 Author

Karthik S

⚠️ License

This project is licensed under the MIT License.
