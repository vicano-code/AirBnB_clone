#!/usr/bin/python3
"""Testing Class: Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_if_str(self):
        """Test if attributes are of type str."""
        review = Review()
        self.assertIsInstance(review.place_id, str, "Expected a string")
        self.assertIsInstance(review.user_id, str, "Expected a string")
        self.assertIsInstance(review.text, str, "Expected a string")

    def test_empty_string(self):
        """Test if attributes are empty strings by default."""
        review = Review()
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
