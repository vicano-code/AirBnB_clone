#!/usr/bin/python3
"""Testing class: Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Sets up Amenity for every test."""
        self.amenity = Amenity()

    def test_amenity_name_string(self):
        """Test if amenity name is a string."""
        self.assertEqual(type(self.amenity.name), str, "Expected a string")

    def test_amenity_empty_str(self):
        """Test if amenity name is an empty string."""
        self.assertEqual(self.amenity.name, "")

    def test_amenity_non_empty_str(self):
        """Test setting a non-empty name for the amenity."""
        self.amenity.name = "Library"
        self.assertEqual(self.amenity.name, "Library")


if __name__ == "__main__":
    unittest.main()
