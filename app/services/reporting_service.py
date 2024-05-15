"""app/services/reporting_service.py Module"""

from app.models.appointment import Appointment
from app.models.patient import Patient

class ReportingService:
    """Reporting Service Class"""
    @staticmethod
    def generate_report():
        """Generate a report"""
        num_appointments = Appointment.query.count()
        num_patients = Patient.query.count()

        return {
            'num_appointments': num_appointments,
            'num_patients': num_patients
        }
