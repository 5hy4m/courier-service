import unittest
from unittest.mock import patch

import os 
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package import Package
from package_manager import PackageManager
from offer import Offer
from vehicle import Vehicle
from main import createOffers

class TestPackageManager(unittest.TestCase):
    offers= [
        {
        "code" :  "OFR001",
        "discount" : "10",
        "ll_distance": "0",
        "ul_distance": "200",
        "ll_weight" : "70",
        "ul_weight" : "200"
        },
        {
            "code" :  "OFR002",
            "discount" : "7",
            "ll_distance": "50",
            "ul_distance": "150",
            "ll_weight" : "100",
            "ul_weight" : "250"
        },
        {
            "code" :  "OFR003",
            "discount" : "5",
            "ll_distance": "50",
            "ul_distance": "250",
            "ll_weight" : "100",
            "ul_weight" : "250"
        }
    ]

    def test_create_package_manager(self):
        with self.assertRaises(ValueError):
            PackageManager(1,'100s',2,0,200)
        with self.assertRaises(ValueError):
            PackageManager(1,'100','2s',0,200)
        with self.assertRaises(ValueError):
            PackageManager(1,'100',2,'0s','200')
        with self.assertRaises(ValueError):
            PackageManager(1,'100',2,0,'200s')
        
        self.assertIsInstance(PackageManager(1,100,2,0,200),PackageManager)

    def test_calculateDeliveryTime(self):
        createOffers(self.offers)
        package = Package(['PKG1' ,'75 ','125','OFR001'])
        
        # Testing the max_speed value
        with self.assertRaises(ZeroDivisionError):
            manager = PackageManager(1,100,2,0,200)
            package.calculateDeliveryTime(manager.current_time,manager.max_speed)

        # Testing the return value
        manager = PackageManager(1,100,2,70,200)
        self.assertEqual(package.calculateDeliveryTime(manager.current_time,manager.max_speed),1.78)

    def test_build2dArray_and_combination(self):
        Vehicle(70,200)
        Vehicle(70,200)
        packages = [
                Package(['PKG1' ,'5', '30', 'OFR001']),
                Package(['PKG2' ,'3', '125', 'OFR008']),
                Package(['PKG3' ,'4', '100', 'OFR003']),
                Package(['PKG4' ,'2', '60', 'OFR002']),
            ] 
        manager = PackageManager(4,100,2,70,6)

        array2D = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 5, 5],
            [0, 0, 0, 3, 3, 5, 5],
            [0, 0, 0, 3, 4, 5, 5],
            [0, 0, 2, 3, 4, 5, 6]
        ]
        
        self.assertEqual(manager.build2dArray(),array2D)
        result = manager.findTheCombination(array2D)

        self.assertEqual([i.name for i in result],[packages[3].name,packages[2].name])

if __name__ == '__main__':
    unittest.main()