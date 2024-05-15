"""app/views/cli/appointment_cli.py Module"""

from flask import current_app
from app.services.appointment_service import AppointmentService

def list_appointments():
    """List all appointments"""
    with current_app.app_context():
        appointments = AppointmentService.get_appointments()
        for appointment in appointments:
            print(appointment.__repr__())

def get_appointment():
    """Get a single appointment by id"""
    with current_app.app_context():
        appointment_id = int(input("Enter appointment ID: "))
        appointment = AppointmentService.get_appointment(appointment_id)
        if appointment:
            print(appointment.__repr__())
        else:
            print("Appointment not found")

def create_appointment():
    """Create a new appointment"""
    with current_app.app_context():
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM:SS): ")
        user_id = int(input("Enter user ID: "))
        patient_id = input("Enter patient ID: ")
        status = input("Enter appointment status: ")

    data = {
        'date': date,
        'time': time,
        'user_id': user_id,
        'patient_id': patient_id,
        'status': status
    }

    appointment = AppointmentService.create_appointment(data)
    print("Appointment created successfully:")
    print(appointment.__repr__())

def update_appointment():
    """Update an existing appointment"""
    with current_app.app_context():
        appointment_id = int(input("Enter appointment ID: "))
        status = input("Enter new status (scheduled/attended/cancelled): ")

        appointment = AppointmentService.get_appointment(appointment_id)
        if appointment:
            appointment.status = status
            AppointmentService.update_appointment(appointment)
            print("Appointment updated successfully.")
        else:
            print("Appointment not found.")