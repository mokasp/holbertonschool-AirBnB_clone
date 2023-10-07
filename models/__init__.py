#!/usr/bin/python3
""" module that loads objects from storage """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
