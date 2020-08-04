import unittest

from pycaching.user import User


class TestUserClass(unittest.TestCase):
    def test_basic_construction(self):
        user = User('Geocaching HQ', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a')

        self.assertEqual(user.name, 'Geocaching HQ')
        self.assertEqual(user.uuid, 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a')

    def test_immutability(self):
        user = User('Geocaching HQ', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a')

        with self.assertRaises(AttributeError):
            user.name = 'value'

        with self.assertRaises(AttributeError):
            user.uuid = 'value'

        with self.assertRaises(AttributeError):
            user.x = 'value'

    def test_uuid_is_required(self):
        with self.assertRaises(ValueError):
            User('Geocaching HQ')

    def test_name_must_by_string(self):
        with self.assertRaises(ValueError):
            User(123)

    def test_lazy_load_from_cache_code(self):
        self.skipTest('why not')
        user = User('Geocaching HQ', lazy_load_from_code="GC8FR0G")

    def test_lazy_load_from_user_code(self):
        self.skipTest('why not')
        user = User('Geocaching HQ', lazy_load_from_code="PRA09E")

    def test_user_equality(self):
        user1 = User('Geocaching HQ', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a')
        user2 = User('Geocaching HQ', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a')

        self.assertEqual(user1, user2)
        self.assertEqual(user1, "Geocaching HQ")

        self.assertNotEqual(user1, User('Geocaching HQ', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382b'))
        self.assertNotEqual(user1, User('Geocaching HQ2', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a'))

    def test_string_operations(self):
        """
        For a backward compatibility we expect that string methods
        should work on User instance as well (on .name).
        """
        user = User('Geocaching HQ', 'cf9c140d-0bad-4e24-9cd2-a16bfc8e382a')

        self.assertEqual(user + 'x', 'Geocaching HQx')
        self.assertEqual('x' + user, 'xGeocaching HQ')

        self.assertEqual(user + user, 'Geocaching HQGeocaching HQ')
        self.assertEqual(2 * user, 'Geocaching HQGeocaching HQ')
        self.assertEqual(user * 2, 'Geocaching HQGeocaching HQ')

        self.assertEqual(len(user), 13)

        self.assertEqual(user.replace(' HQ', ''), 'Geocaching')
        self.assertEqual(user.strip('G'), 'eocaching HQ')

        str_user = str(user)
        self.assertEqual(str_user, 'Geocaching HQ')
        self.assertIsInstance(str_user, str)

        # TODO: self.assertIsInstance(user, str)