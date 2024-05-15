"""tests/test_appointment_service.py Module"""

import unittest
from app import create_app, db
from app.models.appointment import Appointment
from app.services.appointment_service import AppointmentService

class TestAppointmentService(unittest.TestCase):
    """TestAppointmentService Class"""
    def setUp(self):
        """Create a test client"""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_appointments(self):
        """Create test appointments"""
        appointment1 = Appointment(date="2024-05-06", time="09:00:00", user_id=1, status='scheduled')
        appointment2 = Appointment(date="2024-05-07", time="10:00:00", user_id=2, status='scheduled')
        db.session.add_all([appointment1, appointment2])
        db.session.commit()

        appointments = AppointmentService.get_appointments()
        self.assertEqual(len(appointments), 2)

    def test_get_appointment(self):
        """Create a test appointment"""
        appointment = Appointment(date="2024-05-06", time="09:00:00", user_id=1, status='scheduled')
        db.session.add(appointment)
        db.session.commit()

        retrieved_appointment = AppointmentService.get_appointment(appointment.id)
        self.assertEqual(retrieved_appointment.date, "2024-05-06")

    def test_create_appointment(self):
        """Create a test appointment"""
        data = {
            'date': '2024-05-08',
            'time': '11:00:00',
            'user_id': 2,
            'status': 'scheduled'
        }

        appointment = AppointmentService.create_appointment(data)
        self.assertEqual(appointment.date, '2024-05-08')

if __name__ == '__main__':
    unittest.main()
