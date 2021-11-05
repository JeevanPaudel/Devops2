from volume_cuboid import *
import unittest

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1.5)
        self.assertAlmostEqual(cuboid_volume(0),0)
        self.assertAlmostEqual(cuboid_volume(5.5), 166.375)
        self.assertAlmostEqual(cuboid_volume(3), 27)


    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, True)

    def test_int_type(self):
        self.assertIsInstance(cuboid_volume(2), int)

    def test_float_type(self):
        self.assertIsInstance(cuboid_volume(2), float)

    def test_less_equal(self):
        self.assertLessEqual(cuboid_volume(2), 8)
