#!/usr/bin/python3
"""Testing Class: User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def setUp(self):
        """Sets up User for every test."""
        self.user = User()

    def test_user_testing_attributes(self):
        """Test if user attributes are of type str."""
        self.assertIsInstance(self.user.email, str, "Expected a string")
        self.assertIsInstance(self.user.password, str, "Expected a string")
        self.assertIsInstance(self.user.first_name, str, "Expected a string")
        self.assertIsInstance(self.user.last_name, str, "Expected a string")

    def test_user_testing_empty(self):
        """Test if user attributes are empty strings by default."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_non_empty_values(self):
        """Test setting non-empty values for user attributes."""
        self.user.email = "test@example.com"
        self.user.password = "test_Password"
        self.user.first_name = "olawale"
        self.user.last_name = "jackson"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "test_Password")
        self.assertEqual(self.user.first_name, "olawale")
        self.assertEqual(self.user.last_name, "jackson")


if __name__ == "__main__":
    unittest.main()
