import unittest
import os 
import sys
 
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    def test_vehicle_creation(self):
        with self.assertRaises(ValueError):
            Vehicle('4s','4s')

        self.assertIsInstance(Vehicle(4,70),Vehicle)

    

if __name__ == '__main__':
    unittest.main()