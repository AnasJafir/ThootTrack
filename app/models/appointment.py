"""app/models/appointment.py Module"""

from app import db

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    dentist_id = db.Column(db.Integer, db.ForeignKey('dentist.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    status = db.Column(db.Enum('scheduled', 'attended', 'cancelled'), default='scheduled')

    def __repr__(self):
        return f"<Appointment {self.date} {self.time}>"
