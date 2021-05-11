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

    def test_createOffers(self):
        results = createOffers(self.offers)
        self.assertIsInstance(results,list)
        for result in results:
            self.assertIsInstance(result,Offer)

        with self.assertRaises(ValueError):
            createOffers([{
                "code" :  "OFR003",
                "discount" : "DISCOUNT",
                "ll_distance": "50",
                "ul_distance": "250",
                "ll_weight" : "qwerty",
                "ul_weight" : "250"
            }])

if __name__ == '__main__':
    unittest.main()