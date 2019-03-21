import unittest
from betronic import create_app, db
from betronic.user.model import UserModel


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        user = UserModel(login='test.test',
                         email='test@test.ru',
                         password='test')
        self.assertTrue(user.password_hash is not None)

    def test_password_getter(self):
        user = UserModel(
            login='test.test',
            email='test@test.ru',
            password='test')
        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        u = UserModel(
            login='test.test',
            email='test@test.ru',
            password='test')
        self.assertTrue(u.verify_password('test'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        user1 = UserModel(
            login='test.test',
            email='test@test.ru',
            password='test')
        user2 = UserModel(
            login='test.test',
            email='test@test.ru',
            password='test')
        self.assertTrue(user1.password_hash != user2.password_hash)

    def test_role_of_user(self):
        user = UserModel(
            login='test.test',
            email='test@test.ru',
            password='test',
            role='10')
        self.assertTrue(user.role == UserModel.OWNER)
        self.assertFalse(user.role == UserModel.PARTNER)
        self.assertFalse(user.role == UserModel.ADMIN)

    def test_full_name(self):
        user = UserModel(login='test.test',
                         email='test@test.ru',
                         password='test',
                         name="Test",
                         surname="User")
        self.assertTrue(user.full_name == 'Test User')

    def test_full_name_without_surname(self):
        user = UserModel(login='test.test',
                         email='test@test.ru',
                         password='test',
                         name="Test")
        self.assertTrue(user.full_name == 'Test')

    def test_full_name_without_name(self):
        user = UserModel(login='test.test',
                         email='test@test.ru',
                         password='test',
                         surname="Test")
        self.assertTrue(user.surname == 'Test')


if __name__ == "__main__":
    unittest.main()
