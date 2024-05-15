ThootTrack Architecture
======================

Overview
--------

ThootTrack is a dental clinic management system designed to help small dental clinics manage their appointments, patients, and reports efficiently. The system is built using a modular architecture, with separate components for controllers, models, services, and views.

Directory Structure
-------------------

The project is organized into the following directories:

* `app/`: contains the application logic
* `config/`: contains configuration files
* `tests/`: contains unit tests for the application
* `run.py`: the entry point for the application

Application Logic (`app/`)
-------------------------

The `app/` directory contains the following subdirectories:

* `controllers/`: contains controllers for handling user input and interacting with the models
	+ `appointment_controller.py`: handles appointment-related logic
	+ `patient_controller.py`: handles patient-related logic
	+ `user_controller.py`: handles user-related logic
* `models/`: contains data models for the application
	+ `appointment.py`: defines the appointment data model
	+ `patient.py`: defines the patient data model
	+ `user.py`: defines the user data model
* `services/`: contains business logic for the application
	+ `appointment_service.py`: provides appointment-related services
	+ `patient_service.py`: provides patient-related services
	+ `reporting_service.py`: provides reporting services
	+ `user_service.py`: provides user-related services
* `views/`: contains views for rendering user interfaces
	+ `cli/`: contains command-line interface views
		- `appointment_cli.py`: provides appointment-related CLI views
		- `patient_cli.py`: provides patient-related CLI views
		- `user_cli.py`: provides user-related CLI views

Configuration (`config/`)
-------------------------

The `config/` directory contains configuration files for the application, including:

* `database.py`: defines database connection settings

Testing (`tests/`)
--------------

The `tests/` directory contains unit tests for the application, including:

* `test_appointment_service.py`: tests appointment-related services
* `test_reporting_service.py`: tests reporting services
* `test_user_service.py`: tests user-related services

Entry Point (`run.py`)
---------------------

The `run.py` file is the entry point for the application, responsible for initializing the application and starting the CLI.

This architecture provides a clear separation of concerns, with each component responsible for a specific aspect of the application. The modular design allows for easy maintenance and extension of the system.
