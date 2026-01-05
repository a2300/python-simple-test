# How To Use unittest to Write a Test Case for a Function in Python
# https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python

import unittest
import os

class FishTank:
    def __init__(self):
        self.has_water = False
        self.fish_tank_name = "fish_tank.txt"
        default_content = "shark, tuna"
       
        with open(self.fish_tank_name, "w") as f:
            f.write(default_content)

    def fill_with_water(self):
        self.has_water = True

    def empty_tank(self):
        os.remove(self.fish_tank_name)

class TestFishTank(unittest.TestCase):
    def setUp(self):
        self.fish_tank = FishTank()

    def tearDown(self):
        self.fish_tank.empty_tank()

    def test_fish_tank_empty_by_default(self):
        self.assertFalse(self.fish_tank.has_water)

    def test_fish_tank_can_be_filled(self):
        self.fish_tank.fill_with_water()
        self.assertTrue(self.fish_tank.has_water)

    def test_fish_tank_writes_file(self):
        with open(self.fish_tank.fish_tank_name) as f:
            contents = f.read()
        self.assertEqual(contents, "shark, tuna")
