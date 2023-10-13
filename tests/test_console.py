#!/usr/bin/python3
"""This is a Testsuite for the console"""
import json
import os.path
import uuid
from io import StringIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch
from models import storage

from console import HBNBCommand

BASE_DIR = Path(__file__).resolve().parent.parent


class TestConsole(TestCase):
    """Test Engine for the console"""

    file_name = os.path.join(BASE_DIR, 'file.json')

    def setUp(self):
        """Initialization of test instances"""
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
        HBNBCommand().onecmd("destroy User %s" % self.user_id)
        key = 'User.{}'.format(self.user_id)
        self.assertIsNone(storage.all().get(key))
        with open(self.file_name, 'r') as file:
            keys = json.loads(file.read()).keys()
            self.assertNotIn(key, keys)

    def test_destroy_state(self):
        """Tests destroy User instance"""
        HBNBCommand().onecmd("destroy State %s" % self.state_id)
        key = 'State.{}'.format(self.state_id)
        self.assertIsNone(storage.all().get(key))
        with open(self.file_name, 'r') as file:
            keys = json.loads(file.read()).keys()
            self.assertNotIn(key, keys)

    def test_destroy_review(self):
        """Tests destroy Review instance"""
        HBNBCommand().onecmd("destroy Review %s" % self.review_id)
        key = 'Review.{}'.format(self.review_id)
        self.assertIsNone(storage.all().get(key))
        with open(self.file_name, 'r') as file:
            keys = json.loads(file.read()).keys()
            self.assertNotIn(key, keys)

    def test_destroy_place(self):
        """Tests destroy Place instance"""
        HBNBCommand().onecmd("destroy Place %s" % self.place_id)
        key = 'Place.{}'.format(self.place_id)
        self.assertIsNone(storage.all().get(key))
        with open(self.file_name, 'r') as file:
            keys = json.loads(file.read()).keys()
            self.assertNotIn(key, keys)

    def test_destroy_city(self):
        """Tests destroy City instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City %s" % self.city_id)
            key = 'City.{}'.format(self.city_id)
            self.assertIsNone(storage.all().get(key))
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertNotIn(key, keys)

    def test_destroy_base_model(self):
        """Tests destroy BaseModel instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel %s" % self.base_model_id)
            key = 'BaseModel.{}'.format(self.base_model_id)
            self.assertIsNone(storage.all().get(key))
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertNotIn(key, keys)

    def test_destroy_amenity(self):
        """Tests destroy Amenity instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity %s" % self.amenity_id)
            key = 'Amenity.{}'.format(self.amenity_id)
            self.assertIsNone(storage.all().get(key))
            with open(self.file_name, 'r') as file:
                keys = json.loads(file.read()).keys()
                self.assertNotIn(key, keys)

    def test_all_with_invalid_class(self):
        """Tests all with an invalid className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Goat")
            res = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(res, "** class doesn't exist **")

    def test_all_with_valid_class(self):
        """Tests all with a valid className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            res = eval(f.getvalue().strip().split('\n')[-1])
            expected = [str(user) for k, user in storage.all().items() if
                        k.startswith('User.')]
            for i in range(len(expected)):
                self.assertEqual(res[i], expected[i])

    def test_update_without_class(self):
        """Tests update without a className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class name missing **")

    def test_update_with_invalid_class(self):
        """Tests update with an invalid className"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Goat")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** class doesn't exist **")

    def test_update_without_id(self):
        """Tests update without an instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** instance id missing **")

    def test_update_with_invalid_id(self):
        """Tests update with an invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User %s" % str(uuid.uuid4()))
            uid = f.getvalue().strip().split('\n')[-1]
            self.assertEqual(uid, "** no instance found **")

    def test_update_user(self):
        """Tests update User instance"""
        att = 'email'
        value = 'testupdate@alx.org'
        HBNBCommand().onecmd('update User {} {} "{}"'
                             .format(self.user_id, att, value))
        key = 'User.{}'.format(self.user_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)

    def test_update_state(self):
        """Tests update State instance"""
        att = 'name'
        value = 'California'
        HBNBCommand().onecmd('update State {} {} "{}"'
                             .format(self.state_id, att, value))
        key = 'State.{}'.format(self.state_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)

    def test_update_review(self):
        """Tests update Review instance"""
        att = 'user_id'
        value = self.user_id
        HBNBCommand().onecmd('update Review {} {} "{}"'
                             .format(self.review_id, att, value))
        key = 'Review.{}'.format(self.review_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)

    def test_update_place(self):
        """Tests update Place instance"""
        att = 'name'
        value = 'Westlands'
        HBNBCommand().onecmd('update Place {} {} "{}"'
                             .format(self.place_id, att, value))
        key = 'Place.{}'.format(self.place_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)

    def test_update_city(self):
        """Tests update City instance"""
        att = 'name'
        value = 'Paris'
        HBNBCommand().onecmd('update City {} {} "{}"'
                             .format(self.city_id, att, value))
        key = 'City.{}'.format(self.city_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)

    def test_update_base_model(self):
        """Tests update BaseModel instance"""
        att = 'name'
        value = 'Test'
        HBNBCommand().onecmd('update BaseModel {} {} "{}"'
                             .format(self.base_model_id, att, value))
        key = 'BaseModel.{}'.format(self.base_model_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)

    def test_update_amenity(self):
        """Tests update Amenity instance"""
        att = 'name'
        value = 'Swimming pool'
        HBNBCommand().onecmd('update Amenity {} {} "{}"'
                             .format(self.amenity_id, att, value))
        key = 'Amenity.{}'.format(self.amenity_id)
        self.assertEqual(getattr(storage.all().get(key), att), value)
        with open(self.file_name, 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data[key][att], value)
