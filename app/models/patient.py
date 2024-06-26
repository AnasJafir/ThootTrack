"""app/models/patient.py Module"""

from app import db

class Patient(db.Model):
    """Patient Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def __repr__(self):
        """Return a string representation of the patient object"""
        return f"<{self.id} Patient {self.name}>"
