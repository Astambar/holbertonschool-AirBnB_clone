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
class DefaultConsoleTest(unittest.TestCase):
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
        self.assertTrue(console.do_EOF(self,''))
    def test_default_emptyline(self):
        self.assertEqual(console.emptyline(self), None)
    def test_default_quit(self):
        self.assertEqual(console.do_quit(self,''), True)
        self.assertTrue(console.do_quit(self,''))
    def test_default_create(self):
        self.assertEqual(console.do_create(self,'Amenity'), None)
    def test_default_show(self):
        self.assertEqual(console.do_show(self,'Amenity'), None)
    def test_default_destroy(self):
        self.assertEqual(console.do_destroy(self,''), False)
        self.assertFalse(console.do_destroy(self,''))        
    def test_default_update(self):
        self.assertEqual(console.do_update(self,''), False)
        self.assertFalse(console.do_update(self,''))
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)
    def test_default_EOF(self):
        self.assertEqual(console.do_EOF(self,''), True)