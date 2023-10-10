#!/usr/bin/env python
"""__init__  to create a unique FileStorage instance for your application"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
