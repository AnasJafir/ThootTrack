"""app/models/appointment.py Module"""

from app import db

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    status = db.Column(db.Enum('scheduled', 'attended', 'cancelled'), default='scheduled')

    def __repr__(self):
        return f"<{self.id} Appointment {self.date} {self.time} {self.status}>"
