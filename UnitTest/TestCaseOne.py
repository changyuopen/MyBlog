# -*- coding: utf-8 -*-

'''
Created on 2014???10???27???

@author: changyuopen
'''
from DataAccess.ConfigInfoRepository import ConfigInfoRepository
import unittest



class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        self.confgiInfoRepo = ConfigInfoRepository()
        
    def test_shuffle(self):       
        items = self.confgiInfoRepo.getAllConfigInfo()
        self.assertEqual(items.count(), 10, "error length")
        
if __name__ == '__main__':
    unittest.main()
