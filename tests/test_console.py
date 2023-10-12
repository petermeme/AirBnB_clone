#!/usr/bin/python3
"""This is a Testsuite for the console"""
import json
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models import storage

from console import HBNBCommand


class TestConsole(TestCase):
    """Test Engine for the console"""

    file_name = "file.json"

    def setUp(self):
        pass

    def test_create_class_missing(self):
        """Tests creation of BaseModel instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            uid = f.getvalue().strip()
            self.assertEqual(uid, "** class name missing **")

    def test_create_class_not_exist(self):
        """Tests creation of BaseModel instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Goat")
            uid = f.getvalue().strip()
            self.assertEqual(uid, "** class doesn't exist **")

    def test_create_base_model(self):
        """Tests creation of BaseModel instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('BaseModel.{}'.format(uid), keys)

    def test_create_user(self):
        """Tests creation of User instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('User.{}'.format(uid), keys)

    def test_create_state(self):
        """Tests creation of State instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('State.{}'.format(uid), keys)

    def test_create_city(self):
        """Tests creation of City instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('City.{}'.format(uid), keys)

    def test_create_place(self):
        """Tests creation of Place instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('Place.{}'.format(uid), keys)

    def test_create_amenity(self):
        """Tests creation of Amenity instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('Amenity.{}'.format(uid), keys)

    def test_create_review(self):
        """Tests creation of City instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('Review.{}'.format(uid), keys)

