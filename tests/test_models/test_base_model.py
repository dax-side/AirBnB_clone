#!/usr/bin/python3
""" 
    Defines unittests for models/base_model.py

Unittest classes:
        TestBaseModel_instantiation
        TestBaseModel_save
        TestBaseModel_to_dict
"""


import os
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the BaseModel class"""

    def test_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_id_is_unique(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.assertNotEqual(new_model1.id, new_model2.id)

    def test_no_args_instatiation(Self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_created_at_is_datetime(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.assertLess(new_model1, new_model2)

    def test_updated_at_is_datetime(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.assertLess(new_model1, new_model2)

    def test_str_representation(self):
        pass

class TestBaseModel_save(unittest.TestCase):
    """ Unittests for testing the save method of the BaseModel class"""
    pass

class TestBaseModel_to_dict(unittest.TestCase):
    """ Unittests for testing the to_dict method of the BaseModel class"""
    pass


if __name__=="__main__":
    unittest.main()
