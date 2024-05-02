"""app/controllers/appointment_controller.py Module"""

from flask import Blueprint, request, jsonify
from app.services.appointment_service import AppointmentService

bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@bp.route('', methods=['GET'])
def list_appointments():
    appointments = AppointmentService.get_appointments()
    return jsonify({'appointments': [appointment.serialize() for appointment in appointments]})

@bp.route('/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = AppointmentService.get_appointment(appointment_id)
    if appointment:
        return jsonify({'appointment': appointment.serialize()})
    return jsonify({'message': 'Appointment not found'}), 404

@bp.route('', methods=['POST'])
def create_appointment():
    data = request.json
    appointment = AppointmentService.create_appointment(data)
    return jsonify({'message': 'Appointment created successfully', 'appointment': appointment.serialize()}), 201
