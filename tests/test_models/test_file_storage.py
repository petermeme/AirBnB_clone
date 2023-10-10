from unittest import TestCase
from models.base_model import BaseModel
from models import storage

"""This module tests the storage process flow"""


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
        model1 = BaseModel()
        model1.name = "Model 1"
        dict_before = model1.to_dict()
        model1.save()
        storage.reload()
        dict_after = model1.to_dict()
        for k, v in dict_before.items():
            self.assertIn(k, dict_after)
            self.assertTrue(v == dict_after[k] or k == 'updated_at')





