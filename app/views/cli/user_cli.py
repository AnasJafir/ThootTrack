"""app/views/cli/user_cli.py Module"""
from flask import current_app
from app.services.user_service import UserService

def list_users():
    with current_app.app_context():
        users = UserService.get_users()
        for user in users:
            print(user.__repr__())

def get_user():
    with current_app.app_context():
        user_id = int(input("Enter user ID: "))
        user = UserService.get_user(user_id)
        if user:
            print(user.__repr__())
        else:
            print("User not found")

def create_user():
    with current_app.app_context():
        name = input("Enter user name: ")
        role = input("Enter user role: ")
        specialty = input("Enter user specialty (if applicable): ")
        permissions = input("Enter user permissions (if applicable): ")

    data = {
        'name': name,
        'role': role,
        'specialty': specialty,
        'permissions': permissions
    }

    user = UserService.create_user(data)
    print("User created successfully:")
    print(user.__repr__())
