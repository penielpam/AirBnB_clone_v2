#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        do = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", do.__dict__)

    def test_two_amenities_unique_ids(self):
        do1 = Amenity()
        do2 = Amenity()
        self.assertNotEqual(do1.id, do2.id)

    def test_two_amenities_different_created_at(self):
        do1 = Amenity()
        sleep(0.05)
        do2 = Amenity()
        self.assertLess(do1.created_at, do2.created_at)

    def test_two_amenities_different_updated_at(self):
        do1 = Amenity()
        sleep(0.05)
        do2 = Amenity()
        self.assertLess(do1.updated_at, do2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        do = Amenity()
        do.id = "123456"
        do.created_at = do.updated_at = dt
        dostr = do.__str__()
        self.assertIn("[Amenity] (123456)", dostr)
        self.assertIn("'id': '123456'", dostr)
        self.assertIn("'created_at': " + dt_repr, dostr)
        self.assertIn("'updated_at': " + dt_repr, dostr)

    def test_args_unused(self):
        do = Amenity(None)
        self.assertNotIn(None, do.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        do = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(do.id, "345")
        self.assertEqual(do.created_at, dt)
        self.assertEqual(do.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def startUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def pulldown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        do = Amenity()
        sleep(0.05)
        first_updated_at = do.updated_at
        do.save()
        self.assertLess(first_updated_at, do.updated_at)

    def test_two_saves(self):
        do = Amenity()
        sleep(0.05)
        first_updated_at = do.updated_at
        do.save()
        second_updated_at = do.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        do.save()
        self.assertLess(second_updated_at, do.updated_at)

    def test_save_with_arg(self):
        do = Amenity()
        with self.assertRaises(TypeError):
            do.save(None)

    def test_save_updates_file(self):
        do = Amenity()
        do.save()
        doid = "Amenity." + do.id
        with open("file.json", "r") as f:
            self.assertIn(doid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        do = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", do.to_dict())
        self.assertIn("updated_at", do.to_dict())
        self.assertIn("__class__", do.to_dict())

    def test_to_dict_contains_added_attributes(self):
        do = Amenity()
        do.middle_name = "Holberton"
        do.my_number = 98
        self.assertEqual("Holberton", do.middle_name)
        self.assertIn("my_number", do.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        do = Amenity()
        do_dict = do.to_dict()
        self.assertEqual(str, type(do_dict["id"]))
        self.assertEqual(str, type(do_dict["created_at"]))
        self.assertEqual(str, type(do_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        do = Amenity()
        do.id = "123456"
        do.created_at = do.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(do.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        do = Amenity()
        self.assertNotEqual(do.to_dict(), do.__dict__)

    def test_to_dict_with_arg(self):
        do = Amenity()
        with self.assertRaises(TypeError):
            do.to_dict(None)


if __name__ == "__main__":
    unittest.main()
