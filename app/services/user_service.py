"""app/services/user_service.py Module"""

from app import db
from app.models.user import User

class UserService:
    """User Service Class"""
    @staticmethod
    def get_users():
        """Get all users"""
        return User.query.all()

    @staticmethod
    def get_user(user_id):
        """Get a single user by id"""
        return User.query.get(user_id)

    @staticmethod
    def create_user(data):
        """Create a new user"""
        user = User(
            name=data['name'],
            role=data['role'],
            specialty=data.get('specialty'),  # For dentists
            permissions=data.get('permissions')
        )
        db.session.add(user)
        db.session.commit()
        return user
