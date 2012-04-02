# -*- coding: utf-8 -*-
import unittest
import cpghstore

class DumpsTests(unittest.TestCase):
    def assertDumpsMatchesDict(self, s, d):
        pairs = ['"%s"=>%s' % (key, ('"%s"' % value if value is not None else "NULL"))\
                     for key, value in d.iteritems()]
        for pair in pairs:
            self.assertTrue(pair in s)
        self.assertEqual(len(",".join(pairs)), len(s))

    def test_empty(self):
        self.assertEqual(cpghstore.dumps({}), "")

    def test_one(self):
        d = {"key": "value"}
        self.assertDumpsMatchesDict(cpghstore.dumps(d), d)
        d = {"name": "Norge/Noreg"}
        self.assertDumpsMatchesDict(cpghstore.dumps(d), d)

    def test_two(self):
        d = {"key": "value", "key2": "value2"}
        self.assertDumpsMatchesDict(cpghstore.dumps(d), d)

    def test_null(self):
        d = {"key": "value", "key2": "value2", "key3": None}
        self.assertDumpsMatchesDict(cpghstore.dumps(d), d)

    def test_utf8(self):
        d = {"key": "value", "key2": "value2", "key3": None,
             "name": "Noorwe\xc3\xab", "name2": "öäå"}
        self.assertDumpsMatchesDict(cpghstore.dumps(d), d)

    def test_large(self):
        d = {'name:id': 'Norwegia', 'name:cy': 'Norwy', 'name:tr': 'Norve\xc3\xa7', 'official_name:en': 'Kingdom of Norway', 'name:ar': '\xd8\xa7\xd9\x84\xd9\x86\xd8\xb1\xd9\x88\xd9\x8a\xd8\xac', 'name:cs': 'Norsko', 'official_name': 'Kongeriket Norge', 'official_name:lb': 'Kinneksr\xc3\xa4ich Norwegen', 'name:is': 'Noregur', 'name:it': 'Norvegia', 'name:ru': '\xd0\x9d\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x8f', 'name:nl': 'Noorwegen', 'name:pl': 'Norwegia', 'name:fo': 'Noregur', 'name:zh_py': 'Nuowei', 'name:ca': 'Noruega', 'name:af': 'Noorwe\xc3\xab', 'name:vi': 'Na Uy', 'name:fa': '\xd9\x86\xd8\xb1\xd9\x88\xda\x98', 'official_name:sk': 'N\xc3\xb3rske kr\xc3\xa1\xc4\xbeovstvo', 'name:li': 'Noorwege', 'official_name:id': 'Kerajaan Norwegia', 'name:nn': 'Noreg', 'name:haw': 'Nolewai', 'name:fi': 'Norja', 'name:da': 'Norge', 'name:de': 'Norwegen', 'official_name:el': '\xce\x92\xce\xb1\xcf\x83\xce\xaf\xce\xbb\xce\xb5\xce\xb9\xce\xbf \xcf\x84\xce\xb7\xcf\x82 \xce\x9d\xce\xbf\xcf\x81\xce\xb2\xce\xb7\xce\xb3\xce\xaf\xce\xb1\xcf\x82', 'name:fr': 'Norv\xc3\xa8ge', 'official_name:it': 'Regno di Norvegia', 'official_name:be': '\xd0\x9a\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbb\xd0\xb5\xd1\x9e\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0 \xd0\x9d\xd0\xb0\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd1\x96\xd1\x8f', 'name:fy': 'Noarwegen', 'name:mn': '\xd0\x9d\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd0\xb8', 'name:sl': 'Norve\xc5\xa1ka', 'name:lv': 'Norv\xc4\x93\xc4\xa3ija', 'name:ja': '\xe3\x83\x8e\xe3\x83\xab\xe3\x82\xa6\xe3\x82\xa7\xe3\x83\xbc', 'name:lt': 'Norvegija', 'name:no': 'Norge', 'name:nb': 'Norge', 'name:he': '\xd7\xa0\xd7\x95\xd7\xa8\xd7\x95\xd7\x95\xd7\x92\xd7\x99\xd7\x94', 'name:ga': 'An Iorua', 'name:br': 'Norvegia', 'name:lb': 'Norwegen', 'name:la': 'Norvegia', 'name:sk': 'N\xc3\xb3rsko', 'name:uk': '\xd0\x9d\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd1\x96\xd1\x8f', 'name:hy': '\xd5\x86\xd5\xb8\xd6\x80\xd5\xbe\xd5\xa5\xd5\xa3\xd5\xab\xd5\xa1', 'official_name:sv': 'Konungariket Norge', 'name:be': '\xd0\x9d\xd0\xb0\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd1\x96\xd1\x8f', 'name:hu': 'Norv\xc3\xa9gia', 'name:hr': 'Norve\xc5\xa1ka', 'name:el': '\xce\x9d\xce\xbf\xcf\x81\xce\xb2\xce\xb7\xce\xb3\xce\xaf\xce\xb1', 'name:eo': 'Norvegio', 'name:en': 'Norway', 'name': 'Norge/Noreg', 'name:gd': 'Nirribhidh', 'official_name:ja': '\xe3\x83\x8e\xe3\x83\xab\xe3\x82\xa6\xe3\x82\xa7\xe3\x83\xbc\xe7\x8e\x8b\xe5\x9b\xbd', 'name:zh': '\xe6\x8c\xaa\xe5\xa8\x81', 'name:th': '\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb9\x80\xe0\xb8\x97\xe0\xb8\xa8\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xa3\xe0\xb9\x8c\xe0\xb9\x80\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb9\x8c', 'name:sv': 'Norge', 'official_name:vi': 'V\xc6\xb0\xc6\xa1ng qu\xe1\xbb\x91c Na Uy', 'name:et': 'Norra', 'name:zh_pyt': 'Nu\xc3\xb3w\xc4\x93i', 'official_name:lt': 'Norvegijos Karalyst\xc4\x97', 'name:es': 'Noruega'}
        self.assertDumpsMatchesDict(cpghstore.dumps(d), d)
