# app/controllers/patient_controller.py

from flask import Blueprint, request, jsonify
from app.services.patient_service import PatientService

bp = Blueprint('patients', __name__, url_prefix='/patients')

@bp.route('', methods=['GET'])
def list_patients():
    patients = PatientService.get_patients()
    return jsonify({'patients': [patient.__repr__() for patient in patients]})

@bp.route('/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = PatientService.get_patient(patient_id)
    if patient:
        return jsonify({'patient': patient.__repr__()})
    return jsonify({'message': 'Patient not found'}), 404
@bp.route('', methods=['POST'])
def create_patient():
    data = request.json
    patient = PatientService.create_patient(data)
    return jsonify({'message': 'Patient created successfully', 'patient': patient.__repr__()}), 201
