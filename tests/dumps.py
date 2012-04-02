# -*- coding: utf-8 -*-
import unittest
import cpghstore

class DumpsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(cpghstore.dumps({}), "")

    def test_one(self):
        self.assertEqual(
            cpghstore.dumps({"key": "value"}), 
            '"key"=>"value"')

    def test_two(self):
        result = cpghstore.dumps({"key": "value", "key2": "value2"})
        pairs = ['"key"=>"value"', '"key2"=>"value2"']
        for pair in pairs:
            self.assertTrue(pair in result)
        self.assertEqual(len(",".join(pairs)), len(result))

    def test_null(self):
        result = cpghstore.dumps({"key": "value", "key2": "value2", "key3": None})
        pairs = ['"key"=>"value"', '"key2"=>"value2"', '"key3"=>NULL']
        for pair in pairs:
            self.assertTrue(pair in result)
        self.assertEqual(len(",".join(pairs)), len(result))

    def test_utf8(self):
        result = cpghstore.dumps({"key": "value", "key2": "value2", "key3": None,
                                  "name": "Noorwe\xc3\xab", "name2": "öäå"})
        pairs = ['"key"=>"value"', '"key2"=>"value2"', '"key3"=>NULL', 
                 '"name"=>"Noorwe\xc3\xab"', '"name2"=>"öäå"']
        for pair in pairs:
            self.assertTrue(pair in result)
        self.assertEqual(len(",".join(pairs)), len(result))
