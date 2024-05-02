"""tests/test_user_service.py Module """

import unittest
from app import create_app, db
from app.models.user import User
from app.services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_users(self):
        # Create test users
        user1 = User(name="John Doe", role="Receptionist")
        user2 = User(name="Jane Smith", role="Dentist", specialty="Orthodontist")
        db.session.add_all([user1, user2])
        db.session.commit()

        users = UserService.get_users()
        self.assertEqual(len(users), 2)

    def test_get_user(self):
        # Create a test user
        user = User(name="John Doe", role="Receptionist")
        db.session.add(user)
        db.session.commit()

        retrieved_user = UserService.get_user(user.id)
        self.assertEqual(retrieved_user.name, "John Doe")

    def test_create_user(self):
        data = {
            'name': 'Jane Smith',
            'role': 'Dentist',
            'specialty': 'Orthodontist'
        }

        user = UserService.create_user(data)
        self.assertEqual(user.name, 'Jane Smith')

if __name__ == '__main__':
    unittest.main()
