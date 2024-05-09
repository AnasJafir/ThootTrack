# app/views/cli/patient_cli.py
from flask import current_app
from app.services.patient_service import PatientService

def list_patients():
    with current_app.app_context():
        patients = PatientService.get_patients()
        for patient in patients:
            print(patient.__repr__())

def get_patient():
    with current_app.app_context():
        patient_id = int(input("Enter patient ID: "))
        patient = PatientService.get_patient(patient_id)
        if patient:
            print(patient.__repr__())
        else:
            print("Patient not found")

def create_patient():
    with current_app.app_context():
        name = input("Enter patient name: ")
        dob = input("Enter patient date of birth (YYYY-MM-DD): ")
        contact = input("Enter patient contact information: ")
        medical_history = input("Enter patient medical history: ")

    data = {
        'name': name,
        'dob': dob,
        'contact': contact,
        'medical_history': medical_history
    }

    patient = PatientService.create_patient(data)
    print("Patient created successfully:")
    print(patient.__repr__())
