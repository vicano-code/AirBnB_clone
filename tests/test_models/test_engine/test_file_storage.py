#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage
import models

classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage"""

    def setUp(self):
        """Set up method"""
        self.bm_instance = BaseModel()
        self.storage_instance = FileStorage()
        self.user1 = User()

    def test_pep8_conformance(self):
        """Test for PEP8 conformity"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.storage_instance, FileStorage)
        self.assertEqual(type(models.storage).__name__, "FileStorage")
        self.assertEqual(type(self.storage_instance).__name__, "FileStorage")

    def test_method_existence(self):
        """Check if methods exist"""
        storage_instance = FileStorage()
        self.assertTrue(hasattr(storage_instance, "all"))
        self.assertTrue(hasattr(storage_instance, "new"))
        self.assertTrue(hasattr(storage_instance, "save"))
        self.assertTrue(hasattr(storage_instance, "reload"))

    def test_save_method(self):
        """Test save method"""
        self.bm_instance.name = "Pinocho"
        self.bm_instance.save()
        models.storage.reload()
        models.storage.all()
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.bm_instance, 'save'))
        self.assertNotEqual(self.bm_instance.created_at,
                            self.bm_instance.updated_at)

        def test_attributes(self):
            """Test class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(models.storage._FileStorage__objects, dict)
        self.assertIsInstance(models.storage._FileStorage__file_path, str)

    def test_no_arguments(self):
        """Test __init__ with no arguments"""
        try:
            FileStorage()
        except TypeError as e:
            self.fail(f"FileStorage() raised TypeError unexpectedly: {e}")

    def test_arguments(self):
        """Test __init__ with many arguments"""
        with self.assertRaises(TypeError) as error:
            base = FileStorage(7, 12)
        fail = "__init__() takes 1 positional argument but 3 were given"
        self.assertEqual(str(error.exception), fail)

    def test_all_method_return(self):
        """Test if the all method returns a dictionary"""
        file = FileStorage()
        dicto = file.all()
        self.assertIs(dicto, file._FileStorage__objects)
        self.assertIsInstance(dicto, dict)

    def test_new_method(self):
        """Test the new method"""
        file = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = f"{instance.__class__.__name__}.{instance.id}"
                file.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, file._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save_method_to_file(self):
        """Test that save properly saves objects to file.json"""
        file = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = f"{instance.__class__.__name__}.{instance.id}"
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        file.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_pep8_conformance_file_storage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['/models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 1)

    def test_pep8_conformance_test_file(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            '/tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 1)


if __name__ == '__main__':
    unittest.main()
