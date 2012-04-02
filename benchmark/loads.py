# -*- coding: utf-8 -*-
from math import floor

import unittest
import cpghstore
try:
    import pghstore
except ImportError:
    print "INFO: Could not import pghstore (have you done 'pip install pghstore'?)"
    pghstore = None

from benchmark import timefunc

names = [
    '',
    '"name"=>"Norge/Noreg"',
    '"name"=>"Norge/Noreg", "name:af"=>"Noorwe\xc3\xab"',
    '"name"=>"Norge/Noreg", "name:af"=>"Noorwe\xc3\xab", "name:ar"=>NULL',
    '"name"=>"Norge/Noreg", "name:af"=>"Noorwe\xc3\xab", "name:ar"=>"\xd8\xa7\xd9\x84\xd9\x86\xd8\xb1\xd9\x88\xd9\x8a\xd8\xac", "name:be"=>"\xd0\x9d\xd0\xb0\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd1\x96\xd1\x8f", "name:br"=>"Norvegia", "name:ca"=>"Noruega", "name:cs"=>"Norsko", "name:cy"=>"Norwy", "name:da"=>"Norge", "name:de"=>"Norwegen", "name:el"=>"\xce\x9d\xce\xbf\xcf\x81\xce\xb2\xce\xb7\xce\xb3\xce\xaf\xce\xb1", "name:en"=>"Norway", "name:eo"=>"Norvegio", "name:es"=>"Noruega", "name:et"=>"Norra", "name:fa"=>"\xd9\x86\xd8\xb1\xd9\x88\xda\x98", "name:fi"=>"Norja", "name:fo"=>"Noregur", "name:fr"=>"Norv\xc3\xa8ge", "name:fy"=>"Noarwegen", "name:ga"=>"An Iorua", "name:gd"=>"Nirribhidh", "name:he"=>"\xd7\xa0\xd7\x95\xd7\xa8\xd7\x95\xd7\x95\xd7\x92\xd7\x99\xd7\x94", "name:hr"=>"Norve\xc5\xa1ka", "name:hu"=>"Norv\xc3\xa9gia", "name:hy"=>"\xd5\x86\xd5\xb8\xd6\x80\xd5\xbe\xd5\xa5\xd5\xa3\xd5\xab\xd5\xa1", "name:id"=>"Norwegia", "name:is"=>"Noregur", "name:it"=>"Norvegia", "name:ja"=>"\xe3\x83\x8e\xe3\x83\xab\xe3\x82\xa6\xe3\x82\xa7\xe3\x83\xbc", "name:la"=>"Norvegia", "name:lb"=>"Norwegen", "name:li"=>"Noorwege", "name:lt"=>"Norvegija", "name:lv"=>"Norv\xc4\x93\xc4\xa3ija", "name:mn"=>"\xd0\x9d\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd0\xb8", "name:nb"=>"Norge", "name:nl"=>"Noorwegen", "name:nn"=>"Noreg", "name:no"=>"Norge", "name:pl"=>"Norwegia", "name:ru"=>"\xd0\x9d\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x8f", "name:sk"=>"N\xc3\xb3rsko", "name:sl"=>"Norve\xc5\xa1ka", "name:sv"=>"Norge", "name:th"=>"\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb9\x80\xe0\xb8\x97\xe0\xb8\xa8\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xa3\xe0\xb9\x8c\xe0\xb9\x80\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb9\x8c", "name:tr"=>"Norve\xc3\xa7", "name:uk"=>"\xd0\x9d\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd1\x96\xd1\x8f", "name:vi"=>"Na Uy", "name:zh"=>"\xe6\x8c\xaa\xe5\xa8\x81", "name:haw"=>"Nolewai", "name:zh_py"=>"Nuowei", "name:zh_pyt"=>"Nu\xc3\xb3w\xc4\x93i", "official_name"=>"Kongeriket Norge", "official_name:be"=>"\xd0\x9a\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbb\xd0\xb5\xd1\x9e\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0 \xd0\x9d\xd0\xb0\xd1\x80\xd0\xb2\xd0\xb5\xd0\xb3\xd1\x96\xd1\x8f", "official_name:el"=>"\xce\x92\xce\xb1\xcf\x83\xce\xaf\xce\xbb\xce\xb5\xce\xb9\xce\xbf \xcf\x84\xce\xb7\xcf\x82 \xce\x9d\xce\xbf\xcf\x81\xce\xb2\xce\xb7\xce\xb3\xce\xaf\xce\xb1\xcf\x82", "official_name:en"=>"Kingdom of Norway", "official_name:id"=>"Kerajaan Norwegia", "official_name:it"=>"Regno di Norvegia", "official_name:ja"=>"\xe3\x83\x8e\xe3\x83\xab\xe3\x82\xa6\xe3\x82\xa7\xe3\x83\xbc\xe7\x8e\x8b\xe5\x9b\xbd", "official_name:lb"=>"Kinneksr\xc3\xa4ich Norwegen", "official_name:lt"=>"Norvegijos Karalyst\xc4\x97", "official_name:sk"=>"N\xc3\xb3rske kr\xc3\xa1\xc4\xbeovstvo", "official_name:sv"=>"Konungariket Norge", "official_name:vi"=>"V\xc6\xb0\xc6\xa1ng qu\xe1\xbb\x91c Na Uy"'
]

class LoadsBenchmark(unittest.TestCase):
    def test_loads(self):
        n = 10000
        print ""
        for name in names:
            cpg_time = timefunc(cpghstore.loads, n, name)
            if pghstore:
                pg_time = timefunc(pghstore.loads, n, name)
                self.assertTrue(cpg_time < pg_time)
                print ".. n=%i, strlen=%i, cpghstore.loads (%.2fs) is %ix faster than pghstore.loads (%.2fs)" % (
                    n, len(name), cpg_time, floor(pg_time / cpg_time), pg_time)
            else:
                print ".. n=%i, strlen=%i, cpghstore.loads done in %.2fs" % (
                    n, len(name), cpg_time)
