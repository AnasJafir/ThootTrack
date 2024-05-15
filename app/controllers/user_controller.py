"""app/controllers/user_controller.py Module"""

from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET'])
def list_users():
    """List all users"""
    users = UserService.get_users()
    return jsonify({'users': [user.serialize() for user in users]})

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """ Get a single user by id"""
    user = UserService.get_user(user_id)
    if user:
        return jsonify({'user': user.serialize()})
    return jsonify({'message': 'User not found'}), 404

@bp.route('', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.json
    user = UserService.create_user(data)
    return jsonify({'message': 'User created successfully', 'user': user.serialize()}), 201
