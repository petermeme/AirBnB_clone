#!/usr/bin/python3
"""This module tests the storage process flow"""
import unittest
from unittest import TestCase

from models import storage
from models.base_model import BaseModel


class TestFileStorage(TestCase):
    """Test engine for the file storage model"""

    def setUp(self):
        """Initializes the test model"""
        model = BaseModel()
        self.model = model

    def test_new(self):
        """Check whether storage.new() was called during initialization"""
        key = 'BaseModel.{}'.format(self.model.id)
        self.assertIn(key, storage.all().keys())

    def test_save(self):
        """Test saving to file"""
        self.model.save()
        storage.reload()
        key = 'BaseModel.{}'.format(self.model.id)
        self.assertIn(key, storage.all().keys())

    def test_reload_consistency(self):
        """Ensure keys and values remains the same after save/reload"""
        model = BaseModel()
        model.name = "Model 1"
        model.number = 99
        key = 'BaseModel.{}'.format(model.id)
        dict_before = storage.all()[key].to_dict()
        model.save()
        storage.reload()
        dict_after = storage.all()[key].to_dict()
        for k, v in dict_before.items():
            self.assertIn(k, dict_after)
            self.assertTrue(v == dict_after[k] or k == 'updated_at')

    def test_save_custom_attribute(self):
        """Test whether custom attributes are saved"""

        model = BaseModel()
        model.name = "Save me!"
        model.save()
        key = 'BaseModel.{}'.format(model.id)
        self.assertEqual(storage.all()[key].name, "Save me!")
        storage.reload()
        self.assertEqual(storage.all()[key].name, "Save me!")


if __name__ == '__main__':
    unittest.main()
