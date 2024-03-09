#!/usr/bin/python3
"""Testing Class: City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Sets up City for every test."""
        self.city = City()

    def test_city_name_string(self):
        """Test if city name and state ID are strings."""
        self.assertEqual(type(self.city.name), str, "Expected a string")
        self.assertEqual(type(self.city.state_id), str, "Expected a string")

    def test_city_empty_str(self):
        """Test if city name and state ID are empty strings."""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_set_non_empty_name_state_id(self):
        """Test setting a non-empty name and state ID for the city."""
        self.city.name = "New York"
        self.city.state_id = "NY"
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.state_id, "NY")


if __name__ == "__main__":
    unittest.main()
