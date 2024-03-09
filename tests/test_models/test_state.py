#!/usr/bin/python3
"""Test cases for the State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class to test State."""

    def test_string(self):
        """Test if state name is an empty string."""
        state = State()
        self.assertIsInstance(state.name, str, "Expected a string")
        self.assertEqual(state.name, "")

    def test_non_empty_name(self):
        """Test setting a non-empty name for the state."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_id_generation(self):
        """Test if state instances have unique IDs."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_to_dict(self):
        """Test the to_dict() method."""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)

    def test_from_dict(self):
        """Test creating a State instance from a dictionary."""
        state_dict = {"id": "123", "name": "New York"}
        state = State(**state_dict)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.name, "New York")


if __name__ == "__main__":
    unittest.main()
