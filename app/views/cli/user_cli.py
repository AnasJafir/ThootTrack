"""app/views/cli/user_cli.py Module"""

from app.services.user_service import UserService

def list_users():
    users = UserService.get_users()
    for user in users:
        print(user.serialize())

def create_user():
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
    print(user.serialize())
