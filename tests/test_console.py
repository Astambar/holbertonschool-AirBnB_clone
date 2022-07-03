import unittest
import console
import cmd
from models.base_model import BaseModel
import global_usage
from global_usage import *
from models import storage
import models
import shlex
console = console.HBNBCommand

import pycodestyle
from datetime import datetime


class TestHBNBCommand(unittest.TestCase):
    """ Test class HBNBCommand """
    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_prompt(self):
        """test the prompt format"""
        self.assertEqual(console.prompt, "(hbnb) ")

if __name__ == '__main__':
    unittest.main()