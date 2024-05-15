"""app/models/user.py Module"""

from app import db

class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(100), nullable=True)  # For dentists
    permissions = db.Column(db.String(255), nullable=True)

    appointments = db.relationship('Appointment', backref='user', lazy=True)

    def __repr__(self):
        """Return a string representation of the user object"""
        return f"<{self.id} User {self.name}>"
