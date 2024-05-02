"""app/views/cli/appointment_cli.py Module"""

from app.services.appointment_service import AppointmentService

def list_appointments():
    appointments = AppointmentService.get_appointments()
    for appointment in appointments:
        print(appointment.serialize())

def create_appointment():
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM:SS): ")
    user_id = int(input("Enter user ID: "))
    status = input("Enter appointment status: ")

    data = {
        'date': date,
        'time': time,
        'user_id': user_id,
        'status': status
    }

    appointment = AppointmentService.create_appointment(data)
    print("Appointment created successfully:")
    print(appointment.serialize())
