# ThootTrack (Dental Clinic Management System)

ThootTrack is a modern Dental Clinic Management System designed to automate administrative tasks, streamline clinic operations, and improve patient care. This system allows dental clinics to manage appointments, patient records, and more efficiently.

## Features

- Schedule appointments for patients.
- Manage patient records, including medical history and treatment plans.
- Generate reports on key metrics such as the number of appointments and patients.
- Command-line interface (CLI) for easy interaction with the system.

## Technologies Used

- **Python**: The primary programming language for the backend development.
- **Flask**: Micro web framework used for building the backend section.
- **MySQL**: Database management system for storing clinic data.
- **SQLAlchemy**: Object-relational mapping (ORM) library for interacting with the database.
- **Unit Tests**: Testing framework for ensuring the correctness of the application.
- **Git**: Version control system for managing project codebase.

## Project Structure

The project follows a structured layout for better organization and maintenance:

ThootTrack/
│
├── app/ # Application code
│ ├── controllers/ # Controllers for handling HTTP requests
│ ├── models/ # Database models
│ ├── services/ # Business logic services
│ └── views/ # Views for Interface (CLI)
│
├── config/ # Configuration files
├── tests/ # Unit tests
├── README.md # Project documentation
└── run.py # Main entry point for CLI application


## Getting Started

1. Clone the repository:
git clone https://github.com/AnasJafir/ThootTrack.git

2. Install dependencies


3. Set up the database:

   - Update the database configuration in `config/database.py`.
   - Create the database schema:

python -m flask db init
python -m flask db migrate
python -m flask db upgrade

4. Run the application:
python run.py

5. Access the CLI interface and manage appointments and users as needed.


## Testing

To run unit tests:
python -m unittest discover -s tests


## Contributors

- Anas Jafir
