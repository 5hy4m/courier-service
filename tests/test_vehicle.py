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
        with self.assertRaises(ValueError):
            Vehicle('4','4s')

        self.assertIsInstance(Vehicle(4,70),Vehicle)

    def test_getVehicle(self):
        with self.assertRaises(ValueError):
            Vehicle('4s','4s')

        v2 = Vehicle('4','4')
        v2.return_time = 9.9
        v3 = Vehicle('4','4')
        v3.return_time = 9.91
        self.assertEqual(Vehicle.getVehicle(),v2)
    

if __name__ == '__main__':
    unittest.main()