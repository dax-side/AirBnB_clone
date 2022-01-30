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
import time


class TestBaseModel_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the BaseModel class"""

    def test_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_id_of_two_models_is_unique(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.assertNotEqual(new_model1.id, new_model2.id)

    def test_models_different_created_at(self):
        new_model1 = BaseModel()
        time.sleep(0.5)
        new_model2 = BaseModel()
        self.assertNotEqual(new_model1.created_at, new_model2.created_at)

    def test_models_different_updated_at(self):
        new_model1 = BaseModel()
        time.sleep(0.5)
        new_model2 = BaseModel()
        self.assertNotEqual(new_model1.updated_at, new_model2.updated_at)

    def test_no_args_instatiation(Self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_created_at_is_datetime(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.assertLess(new_model1, new_model2)

    def test_updated_at_is_datetime(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.assertLess(new_model1, new_model2)

    def test_str_representation(self):
        dt = datetime.now()
        # show the official datetime object representation as a string
        dt_repr = repr(dt)
        nm = BaseModel()
        nm.id = "1234"
        nm.created_at = nm.updated_at = dt
        nm_str = nm.__str__()
        self.assertIn("[BaseModel] (1234)", nm_str)
        self.assertIn("'id': '1234'", nm_str)
        self.assertIn("'created_at': " + dt_repr, nm_str)
        self.assertIn("'updated_at': " + dt_repr, nm_str)

    def test_unused_args(self):
        new_model = BaseModel(None)
        self.assertNotIn(None, new_model.__dict__.values())

    def test_instantiate_with_kwarg(self):
        dt = datetime.now()
        dt_iso = dt.isoformart()
        new_model = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(new_model.id, "123")
        self.assertEqual(new_model.created_at, dt)
        self.asserteEqual(new_model.updated_at, dt)

    def test_instantiate_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiate_with_args_and_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoforat()
        nm = BaseModel("10", d="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(nm.id, "123")
        self.assertEqual(nm.created_at, dt)
        self.assertEqual(nm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """ Unittests for testing the save method of the BaseModel class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        nm = BaseModel()
        time.sleep(0.0)
        first_update = nm.updated_at
        nm.save()
        self.assertLess(first_update, nm.updated_at)

    def test_save_twice(self):
        nm = BaseModel()
        time.sleep(0.05)
        first_update = nm.updated_at
        nm.save()
        second_update = nm.updated_at
        self.assertLess(first_update, second_update)
        time.sleep(0.05)
        nm.save()
        self.assertLess(second_update, nm.updated_at)

    def test_save_with_arg(self):
        nm = BaseModel()
        with self.assertRaises(TypeError):
            nm.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """ Unittests for testing the to_dict method of the BaseModel class"""

    def test_to_dict_type(self):
        nm = BaseModel()
        self.assertTrue(dict, type(nm.to_dict()))

    def test_to_dict_datetime_objects_are_strs(self):
        nm = BaseModel()
        nm_dict = nm.to_dict()
        self.assertEqual(str, type(nm_dict["created_at"]))
        self.assertEqual(str, type(nm_dict["updated_at"]))

    def test_to_dict_has_correct_keys(self):
        nm = BaseModel()
        self.assertIn("id", nm.to_dict())
        self.assertIn("created_at", nm.to_dict())
        self.assertIn("updated_at", nm.to_dict())
        self.assertIn("__class__", nm.to_dict())

    def test_to_dict_contains_added_attrbutes(self):
        nm = BaseModel()
        nm.name = "my_first_model"
        nm.my_number = 89
        self.assertIn("name", nm.to_dict())
        self.assertIn("my_number", nm.to_dict())

    def test_to_dict_output(self):
        dt = datetime.now()
        nm = BaseModel()
        nm.id = "1234"
        nm.created_at = nm.updated_at = dt
        out_dict = {
                'id': '1234',
                '__class__': 'BaseModel',
                'created_at': dt.isoformat()
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(nm.to_dict(), out_dict)

    def test_to_dict_with_arg(self):
        nm = BaseModel()
        with self.assertRaises(TypeError):
            nm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
