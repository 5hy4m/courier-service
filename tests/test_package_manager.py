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
            PackageManager('100s',2,0,200)
        with self.assertRaises(ValueError):
            PackageManager('100','2s',0,200)
        with self.assertRaises(ValueError):
            PackageManager('100',2,'0s','200')
        with self.assertRaises(ValueError):
            PackageManager('100',2,0,'200s')
        
        self.assertIsInstance(PackageManager(100,2,0,200),PackageManager)

    def test_truncate(self):
        self.assertEqual(PackageManager.truncate(17.9999,2),17.99)
        self.assertEqual(PackageManager.truncate(17.1111,2),17.11)
        self.assertEqual(PackageManager.truncate(17.19,2),17.19)
        self.assertEqual(PackageManager.truncate(17,2),17.00)

    def test_calculateDeliveryTime(self):
        createOffers(self.offers)
        package = Package(['PKG1' ,'75 ','125','OFR001'])
        
        # Testing the max_speed value
        with self.assertRaises(ZeroDivisionError):
            manager = PackageManager(100,2,0,200)
            manager.calculateDeliveryTime(package)

        # Testing the return value
        manager = PackageManager(100,2,70,200)
        self.assertEqual(manager.calculateDeliveryTime(package),1.78)

    @patch('builtins.print')
    def test_calculateTimeTaken(self,mock_print):
        Vehicle(2,70)
        packages = [
                # Package(['PKG1' ,'5', '5', 'OFR001']),
                Package(['PKG2' ,'75', '125', 'OFR001']),
                # Package(['PKG3' ,'50', '30', 'OFR001']),
            ]
        manager = PackageManager(100,2,10,200)
        manager.calculateTimeTaken(packages)
        mock_print.assert_called_with('PKG2 147.5 1327.5', 12.5)
        pass


if __name__ == '__main__':
    unittest.main()