"""tests/test_reporting_service.py Module"""

import unittest
from app import create_app, db
from app.models.appointment import Appointment
from app.models.patient import Patient
from app.services.reporting_service import ReportingService

class TestReportingService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_generate_report(self):
        # Create test appointments and patients
        appointment1 = Appointment(date="2024-05-06", time="09:00:00", user_id=1, status='scheduled')
        appointment2 = Appointment(date="2024-05-07", time="10:00:00", user_id=2, status='scheduled')
        patient1 = Patient(name="John Doe", dob="1990-01-01", contact="1234567890")
        patient2 = Patient(name="Jane Smith", dob="1985-05-05", contact="9876543210")
        db.session.add_all([appointment1, appointment2, patient1, patient2])
        db.session.commit()

        report = ReportingService.generate_report()
        self.assertEqual(report['num_appointments'], 2)
        self.assertEqual(report['num_patients'], 2)

if __name__ == '__main__':
    unittest.main()
