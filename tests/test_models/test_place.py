#!/usr/bin/python3
"""Testing Class: Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_place_for_type(self):
        """Test if attributes have correct types."""
        place = Place()
        self.assertIsInstance(place.city_id, str, "Expected a string")
        self.assertIsInstance(place.user_id, str, "Expected a string")
        self.assertIsInstance(place.name, str, "Expected a string")
        self.assertIsInstance(place.description, str, "Expected a string")
        self.assertIsInstance(place.number_rooms, int, "Expected integer")
        self.assertIsInstance(place.number_bathrooms, int, "Expected integer")
        self.assertIsInstance(place.max_guest, int, "Expected integer")
        self.assertIsInstance(place.price_by_night, int, "Expected integer")
        self.assertIsInstance(place.latitude, float, "Expected a float")
        self.assertIsInstance(place.longitude, float, "Expected a float")
        self.assertIsInstance(place.amenity_ids, list, "Expected a list")

    def test_empty_string(self):
        """Test if attributes have empty string by default."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")

    def test_place_for_zero(self):
        """Test if integer attributes are set to zero by default."""
        place = Place()
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)

    def test_place_for_float(self):
        """Test if float attributes are set to zero by default."""
        place = Place()
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)

    def test_for_empty_list(self):
        """Test if amenity_ids is an empty list by default."""
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
