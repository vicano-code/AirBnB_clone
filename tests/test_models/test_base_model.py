#!usr/bin/python3
""" Test BaseModel """
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a clean instance of BaseModel before each test.
        """
        self.base_model = BaseModel()

    def test_id_type(self):
        """
        Test if the id attribute is of type string.
        """
        self.assertEqual(type(self.base_model.id), str)

    def test_id_len(self):
        """
        Test the length of the id attribute (should be 36 characters long).
        """
        self.assertEqual(len(self.base_model.id), 36)

    def test_unique_id(self):
        """
        Test if each instance of BaseModel has a unique id.
        """
        self.base_model_1 = BaseModel()
        self.assertNotEqual(self.base_model.id, self.base_model_1.id)

    def test_created_at_type(self):
        """
        Test if the created_at attribute is an instance of datetime.
        """
        self.assertTrue(isinstance(self.base_model.created_at, datetime))

    def test_updated_at_type(self):
        """
        Test if the updated_at attribute is an instance of datetime.
        """
        self.assertTrue(isinstance(self.base_model.updated_at, datetime))

    def test_updated_at_changes(self):
        """
        Test if the updated_at attribute changes after calling save().
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_str(self):
        """
        Test the __str__ method to ensure it returns expected string format.
        """
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_return(self):
        """
        Test the return value of the to_dict() method.
        """
        test_dict = self.base_model.to_dict()
        self.assertTrue(type(test_dict) is dict)

    def test_to_dict_no_dunder(self):
        """
        Test if the dictionary returned by to_dict()
        does not contain any dunder attributes.
        """
        dunder = self.base_model.__dict__
        for attr in dunder.keys():
            self.assertNotIn('__', attr)

    def test_to_dict_class(self):
        """
        Test if the __class__ key is present in the dictionary returned
        by to_dict().
        """
        test_dict = self.base_model.to_dict()
        self.assertIn("__class__", test_dict)

    def test_to_dict_custom_attribute(self):
        """
        Test if custom attributes added to the BaseModel instance
        are included in the dictionary returned by to_dict().
        """
        self.base_model.custom_attribute = "test"
        base_dict = self.base_model.to_dict()
        self.assertIn("custom_attribute", base_dict)

    def test_to_dict_updated_at_type(self):
        """
        Test if the updated_at attribute in the dictionary returned
        by to_dict() is a string.
        """
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict["updated_at"], str)

    def test_to_dict_created_at(self):
        """
        Test if the created_at attribute in the dictionary returned
        by to_dict() is a string.
        """
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict["created_at"], str)

    def test_save_updated_at_type(self):
        """
        Test if the updated_at attribute after calling save()
        is an instance of datetime.
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertNotEqual(str(initial_updated_at),
                            str(self.base_model.updated_at))


if __name__ == "__main__":
    unittest.main()
