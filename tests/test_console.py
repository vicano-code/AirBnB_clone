#!/usr/bin/python3
"""Defines unittests for console.py."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        h = "Quits the command interpreter"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = ("Usage: create <class>\n        "
             "Create a new instance of a class and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "exit program on EOF command - Ctrl-D(linux), Ctrl-Z(Windows)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Usage: destroy <class> <id>\n        "
             "Deletes an instance based on the class name and id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("Usage: all [class]\n        "
             "Prints all string representations of all instances.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Updates an instance based on the class name and id by adding or\
             updating attribute (save the change into the JSON file).\n"
             "Ex: $ update BaseModel 1234-1234-1234 email \"aibnb@mail.com\"")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_operations(unittest.TestCase):
    """
    Unittests for testing command operations of the
    HBNB command interpreter.
    """

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("create NotAClass")
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())
        with patch("sys.stdout", new=StringIO()) as output:
            self.typing.onecmd("create BaseModel")
            self.assertTrue(len(output.getvalue().strip()) > 0)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("show User")
            self.assertEqual("** instance id missing **\n",
                             output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("User.show()")
            self.assertEqual("** instance id missing **\n",
                             output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("show User '999'")
            self.assertEqual("** no instance found **\n",
                             output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("BaseModel.show('999')")
            self.assertEqual("** no instance found **\n",
                             output.getvalue())
        with patch("sys.stdout", new=StringIO()) as output:
            self.typing.onecmd("create BaseModel")
            obj_id = output.getvaue()
            self.typing.onecmd("show BaseModel obj_id")
            self.assertTrue(len(output.getvalue().strip()) > 0)

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd
                             ("destroy BaseModel 1234-1234-1234"))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertTrue(len(output.getvalue().strip()) > 0)

    def test_update(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel\
                             1234-1234-1234 name 'new_name'"))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
