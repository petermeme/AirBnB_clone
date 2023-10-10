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
        self.assertIn(key, list(storage.all().keys()))

    def test_save(self):
        """Test saving to file"""
        self.model.save()
        storage.reload()
        key = 'BaseModel.{}'.format(self.model.id)
        self.assertIn(key, list(storage.all().keys()))
