import unittest
import os 
import sys
 
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package import Package
from offer import Offer
from main import createOffers

class TestPackage(unittest.TestCase):
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
            "ll_weight" : "10",
            "ul_weight" : "150"
        }
    ]

    def test_createPackages(self):
        createOffers(self.offers)
        with self.assertRaises(ValueError):
            Package(['PKG1' ,'50S', '30', 'OFR001'])
            Package(['PKG2' ,'50', '30E', 'OFR001'])
        
        self.assertIsInstance(Package(['PKG1' ,'50', '30', 'OFR001']),Package)
    
    def test_get_weights_in_asc_order(self):
        createOffers(self.offers)
        Package(['PKG1' ,'0', '30', 'OFR001'])
        Package(['PKG1' ,'20', '30', 'OFR001'])
        Package(['PKG1' ,'0', '30', 'OFR001'])
        Package(['PKG1' ,'100', '30', 'OFR001'])
        Package(['PKG1' ,'0', '30', 'OFR001'])

        # Check if it returns a list
        self.assertIsInstance(Package.get_weights(),list)

        results = Package.get_weights()

        # Check if it returns a list of Offer Class Instances
        for result in results:
            self.assertIsInstance(result,Offer)

        # Check if it returns a list of Offer Class Instances are in ascending order
        weight = 0
        for package in results:
            self.assertTrue(weight <= package.weight)
            weight = package.weight

    def test_summation_of_the_array(self):
        self.assertEqual(Package.summationOfTheArray([166,616,61,0,1,5]),849)
        self.assertEqual(Package.summationOfTheArray([-20,10,30,0]),20)

    def test_calculateDeliveryCost(self):
        createOffers(self.offers)
        self.assertEqual(
            Package(['PKG1' ,'5', '5', 'OFR001']).calculateDeliveryCost(100),
            'PKG1 0 175'
            )

        self.assertEqual(
            Package(['PKG2' ,'15', '5', 'OFR002']).calculateDeliveryCost(100),
            'PKG2 0 275'
            )

        self.assertEqual(
            Package(['PKG3' ,'10', '100', 'OFR003']).calculateDeliveryCost(100),
            'PKG3 35 665'
            )
        
        self.assertEqual(
            Package(['PKG4' ,'50', '30', 'OFR001']).calculateDeliveryCost(100),
            'PKG4 0 750'
            )

        self.assertEqual(
            Package(['PKG4' ,'75', '125', 'OFFR0008']).calculateDeliveryCost(100),
            'PKG4 0 1475'
            )

        self.assertEqual(
            Package(['PKG4' ,'175', '100', 'OFFR003']).calculateDeliveryCost(100),
            'PKG4 0 2350'
            )
        
        self.assertEqual(
            Package(['PKG4' ,'110', '60', 'OFFR002']).calculateDeliveryCost(100),
            'PKG4 0 1500'
            )

        self.assertEqual(
            Package(['PKG4' ,'155', '95', 'OFFR003']).calculateDeliveryCost(100),
            'PKG4 0 2125'
            )

if __name__ == '__main__':
    unittest.main()