# #!/usr/bin/python3
# """ Module for testing file storage"""
# import unittest
# from models.engine.db_storage import DBStorage
# import os
# import MySQLdb
# from models.base_model import BaseModel
# # from console import HBNBCommand


# @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
#                  'fileStorage test not supported')
# class test_dbStorage(unittest.TestCase):
#     """ Class to test the file storage method """

#     def setUp(self):
#         """ Set up test environment """
#         self.db = MySQLdb.connect(user='hbnb_test',
#                                   passwd='hbnb_test_pwd',
#                                   host='localhost',
#                                   db='hbnb_test_db')
#         self.cursor = self.db.cursor()
#         self.storage = DBStorage()
#         self.storage.reload()

#     def tearDown(self):
#         """ Remove storage file at end of tests """
#         try:
#             self.db = MySQLdb.connect(user='hbnb_test',
#                                       passwd='hbnb_test_pwd',
#                                       host='localhost',
#                                       db='hbnb_test_db')
#             self.cursor = self.db.cursor()
#             self.cursor.execute("SHOW TABLES")
#             tables = self.cursor.fetchall()
#             for table_name in tables:
#                 self.cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]}")
#             self.db.commit()
#         except Exception:
#             pass

#     def test_tables_empty(self):
#         """ tables are initially empty """
#         self.cursor.execute("SHOW TABLES")
#         tables = self.cursor.fetchall()
#         for table_name in tables:
#             self.cursor.execute(f"SELECT * FROM {table_name[0]}")
#             table = self.cursor.fetchall()
#             self.assertEqual(len(table), 0)

#     def test_new(self):
#         """ New object is correctly added to a session """
#         new_item = BaseModel()
#         self.storage.new(new_item)
#         self.assertIn(new_item, self.storage.__session.new)

#     def test_all(self):
#         """ all table values are properly returned """
#         new_item1 = BaseModel()
#         new_item2 = BaseModel()
#         new_item3 = BaseModel()
#         self.storage.new(new_item1)
#         self.storage.new(new_item2)
#         self.storage.new(new_item3)
#         self.storage.save()
#         result = self.storage.all(BaseModel)
#         self.assertIsInstance(result, dict)
#         self.assertIn(new_item1, result.values())
#         self.assertIn(new_item2, result.values())
#         self.assertIn(new_item3, result.values())

#     def test_save(self):
#         """ DBStorage save method """
#         new_item = BaseModel()
#         self.storage.new(new_item)
#         self.storage.save()
#         result = self.storage.all(BaseModel).values()
#         self.assertIn(new_item, result)

#     # def test_reload(self):
#     #     """ Storage file is successfully loaded to __objects """
#     #     new = BaseModel()
#     #     storage.save()
#     #     storage.reload()
#     #     for obj in storage.all().values():
#     #         loaded = obj
#     #     self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

#     # def test_reload_empty(self):
#     #     """ Load from an empty file """
#     #     with open('file.json', 'w') as f:
#     #         pass
#     #     with self.assertRaises(ValueError):
#     #         storage.reload()

#     # def test_reload_from_nonexistent(self):
#     #     """ Nothing happens if file does not exist """
#     #     self.assertEqual(storage.reload(), None)

#     # def test_base_model_save(self):
#     #     """ BaseModel save method calls storage save """
#     #     new = BaseModel()
#     #     new.save()
#     #     self.assertTrue(os.path.exists('file.json'))

#     # def test_delete(self):
#     #     # Test removing an existing object

#     #     # create object
#     #     new_obj = HBNBCommand().onecmd('create Place city_id=123')
#     #     # get number of items before storage
#     #     old_objs = len(storage.all())
#     #     storage.delete(new_obj)
#     #     all_objs = len(storage.all())
#     #     self.assertEqual(all_objs, old_objs - 1)
