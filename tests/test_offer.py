import unittest
import os 
import sys
 
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from package import Package
from offer import Offer
from main import createOffers


class TestOffer(unittest.TestCase):
    offers= [{
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
    }]

    offers_objects = []

    def test_createOffers(self):
        with self.assertRaises(ValueError):
            createOffers([{
                "code" :  "OFR003",
                "discount" : "DISCOUNT",
                "ll_distance": "50",
                "ul_distance": "250",
                "ll_weight" : "qwerty",
                "ul_weight" : "250"
            }])
        
        results = createOffers(self.offers)
        self.assertIsInstance(results,list)
        for result in results:
            self.assertIsInstance(result,Offer)
        self.offers_objects.extend(results)
    
    def test_createPackages(self):
        createOffers(self.offers)
        with self.assertRaises(ValueError):
            Package(['PKG1' ,'50S', '30', 'OFR001'])
            Package(['PKG2' ,'50', '30E', 'OFR001'])
        
        self.assertIsInstance(Package(['PKG1' ,'50', '30', 'OFR001']),Package)

    def test_get_object(self):
        createOffers(self.offers)
        self.assertIsInstance(Offer.get_object('OFR001'),Offer)
        self.assertIsInstance(Offer.get_object('OFR002'),Offer)
        self.assertIsInstance(Offer.get_object('OFR003'),Offer)
        
    def test_checkOffers(self):
        createOffers(self.offers)
        package = Package(['PKG1' ,'5', '5', 'OFR001'])
        self.assertEqual(package.checkOffer(),False)

        package = Package(['PKG1' ,'70', '5', 'OFR001'])
        self.assertEqual(package.checkOffer(),True)

        pass

if __name__ == '__main__':
    unittest.main()