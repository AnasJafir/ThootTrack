"""app/services/appointment_service.py Module"""

from app import db
from app.models.appointment import Appointment

class AppointmentService:
    """Appointment Service Class"""
    @staticmethod
    def get_appointments():
        """Get all appointments"""
        return Appointment.query.all()

    @staticmethod
    def get_appointment(appointment_id):
        """Get a single appointment by id"""
        return Appointment.query.get(appointment_id)

    @staticmethod
    def create_appointment(data):
        """Create a new appointment"""
        appointment = Appointment(
            date=data['date'],
            time=data['time'],
            user_id=data['user_id'],
            patient_id=data['patient_id'],
            status=data['status']
        )
        db.session.add(appointment)
        db.session.commit()
        return appointment
    
    @staticmethod
    def update_appointment(appointment):
        """Update an existing appointment"""
        db.session.commit()
        return appointment
