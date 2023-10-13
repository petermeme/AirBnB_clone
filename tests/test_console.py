#!/usr/bin/python3
"""This is a Testsuite for the console"""
import json
import uuid
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models import storage

from console import HBNBCommand


class TestConsole(TestCase):
    """Test Engine for the console"""

    file_name = "file.json"

    def setUp(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.user_id = f.getvalue().strip().split('\n')[-1]
            HBNBCommand().onecmd("create State")
            self.state_id = f.getvalue().strip().split('\n')[-1]
            HBNBCommand().onecmd("create Review")
            self.review_id = f.getvalue().strip().split('\n')[-1]
            HBNBCommand().onecmd("create Place")
            self.place_id = f.getvalue().strip().split('\n')[-1]
            HBNBCommand().onecmd("create City")
            self.city_id = f.getvalue().strip().split('\n')[-1]
            HBNBCommand().onecmd("create BaseModel")
            self.base_model_id = f.getvalue().strip().split('\n')[-1]
            HBNBCommand().onecmd("create Amenity")
            self.amenity_id = f.getvalue().strip().split('\n')[-1]

    def test_create_without_class(self):
        """Tests create without a className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class name missing **")

    def test_create_with_invalid_class(self):
        """Tests create with an invalid className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Goat")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class doesn't exist **")

    def test_create_user(self):
        """Tests creation of User instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('User.{}'.format(uid), keys)

    def test_create_state(self):
        """Tests creation of State instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('State.{}'.format(uid), keys)

    def test_create_review(self):
        """Tests creation of City instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('Review.{}'.format(uid), keys)

    def test_create_place(self):
        """Tests creation of Place instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('Place.{}'.format(uid), keys)

    def test_create_city(self):
        """Tests creation of City instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('City.{}'.format(uid), keys)

    def test_create_base_model(self):
        """Tests creation of BaseModel instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('BaseModel.{}'.format(uid), keys)

    def test_create_amenity(self):
        """Tests creation of Amenity instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertTrue(len(uid) == 36)  # a uuid4 string
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertIn('Amenity.{}'.format(uid), keys)

    def test_show_without_class(self):
        """Tests show without a className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class name missing **")

    def test_show_with_invalid_class(self):
        """Tests show with invalid className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Goat")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class doesn't exist **")

    def test_show_without_id(self):
        """Tests show without an instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** instance id missing **")

    def test_show_with_invalid_id(self):
        """Tests show with an invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User %s" % str(uuid.uuid4()))
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** no instance found **")

    def test_show_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User %s" % self.user_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'User.{}'.format(self.user_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_show_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State %s" % self.state_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'State.{}'.format(self.state_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_show_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review %s" % self.review_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'Review.{}'.format(self.review_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_show_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place %s" % self.place_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'Place.{}'.format(self.place_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_show_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City %s" % self.city_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'City.{}'.format(self.city_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_show_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel %s" % self.base_model_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'BaseModel.{}'.format(self.base_model_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_show_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity %s" % self.amenity_id)
            res = f.getvalue().strip().split('\n')[-1]
            key = 'Amenity.{}'.format(self.amenity_id)
            expected = str(storage.all().get(key))
            self.assertEqual(res, expected)

    def test_destroy_without_class(self):
        """Tests destroy without className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class name missing **")

    def test_destroy_with_invalid_class(self):
        """Tests destroy with invalid className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Goat")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class doesn't exist **")

    def test_destroy_without_id(self):
        """Tests destroy without an instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** instance id missing **")

    def test_destroy_with_invalid_id(self):
        """Tests destroy with an invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User %s" % str(uuid.uuid4()))
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** no instance found **")

    def test_destroy_user(self):
        """Tests destroy User instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User %s" % self.user_id)
            key = 'User.{}'.format(self.user_id)
            self.assertIsNone(storage.all().get(key))
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertNotIn(key, keys)

    def test_destroy_state(self):
        """Tests destroy User instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State %s" % self.state_id)
            key = 'State.{}'.format(self.state_id)
            self.assertIsNone(storage.all().get(key))
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertNotIn(key, keys)

    def test_destroy_review(self):
        """Tests destroy Review instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review %s" % self.review_id)
            key = 'Review.{}'.format(self.review_id)
            self.assertIsNone(storage.all().get(key))
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertNotIn(key, keys)
