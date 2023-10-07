#!/usr/bin/python3
""" module that loads objects from JSON file"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
