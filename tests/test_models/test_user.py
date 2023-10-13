#!/usr/bin/python3
"""This module tests the User Model"""
import json
import os
import unittest
from datetime import datetime
from unittest import TestCase
from models.user import User
from tests import BASE_DIR


class TestUser(TestCase):
    """Test engine for user model"""

    file_name = os.path.join(BASE_DIR, 'file.json')

    def setUp(self):
        """Creates a user object for testing"""
        user = User()
        user.first_name = "Test"
        user.last_name = "User"
        user.email = "test@mail.com"
        user.password = "root"
        self.user = user

    def test_id_validity(self):
        """Tests the validity of instance id"""
        self.assertEqual(type(self.user.id), str)
        self.assertEqual(len(self.user.id), 36)

    def test_dates_types(self):
        """Are they actual dates?"""
        self.assertEqual(type(self.user.created_at), datetime)
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_date_equality_during_initialization(self):
        """
        created_at and updated-at should be the same after
        initialization
        """
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_str(self):
        """Tests the verbose representation of a User"""
        self.assertEqual(str(self.user),
                         f"[User] ({self.user.id})"
                         f" {self.user.__dict__}")

    def test_date_change_on_save(self):
        """Ensure updated_at is changed to a future date on save"""
        self.assertEqual(self.user.created_at, self.user.updated_at)
        self.user.save()
        self.assertTrue(self.user.updated_at > self.user.created_at)

    def test_all_keys_present(self):
        """Ensure all expected keys are present in our custom dict"""
        expected_keys = ['email', 'password', 'first_name', 'last_name',
                         'email', '__class__', 'password']
        model_dict = self.user.to_dict()
        for k in expected_keys:
            self.assertIn(k, model_dict.keys())

    def test_dict_content(self):
        """ Validates the result of to_dict"""
        vals = self.user.to_dict()
        self.assertEqual(self.user.created_at.isoformat(),
                         vals.get('created_at'))
        self.assertEqual(self.user.updated_at.isoformat(),
                         vals.get('updated_at'))
        self.assertEqual('User', vals.get('__class__'))
        self.assertEqual(self.user.id, vals.get('id'))
        self.assertEqual(self.user.first_name, vals['first_name'])
        self.assertEqual(self.user.last_name, vals['last_name'])
        self.assertEqual(self.user.email, vals['email'])
        self.assertEqual(self.user.password, vals['password'])

    def test_initialization_with_kwargs(self):
        """Ascertains that we are able to recreate
        an object given its dict representation"""
        kw = self.user.to_dict()
        user = User(**kw)
        for k, v in user.to_dict().items():
            self.assertEqual(kw[k], v)

    def test_save(self):
        """Test whether User object is successfully saved when save() is
        called"""
        user = User()
        user.save()
        key = "User.{}".format(user.id)
        with open(self.file_name, 'r') as f:
            data = json.loads(f.read() or "{}")
            self.assertIn(key, data.keys())


if __name__ == '__main__':
    unittest.main()
