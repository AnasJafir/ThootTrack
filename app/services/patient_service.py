"""app/services/patient_service.py"""

from app import db
from app.models.patient import Patient

class PatientService:
    """Patient Service Class"""
    @staticmethod
    def get_patients():
        """Get all patients"""
        return Patient.query.all()

    @staticmethod
    def get_patient(patient_id):
        """Get a single patient by id"""
        return Patient.query.get(patient_id)
    @staticmethod
    def create_patient(data):
        """Create a new patient"""
        patient = Patient(
            name=data['name'],
            dob=data['dob'],
            contact=data['contact'],
            medical_history=data.get('medical_history')
        )
        db.session.add(patient)
        db.session.commit()
        return patient
