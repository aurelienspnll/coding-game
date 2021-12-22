import unittest
import world

"""
World definiton:
##########
#    T   #
#        #
#        #
#     X  #
#@    X  #
#     X  #
#        #
#    T  $#
##########
"""

class TestUtils(unittest.TestCase):
    def setUp(self):
        world_def = "###########    T   ##        ##        ##     X  ##@    X  ##     X  ##        ##    T  $###########"
        self.world = world.World(10, 10, world_def)

    def test_get_start_position(self):
        self.assertEqual(self.world.get_start_position(), (5, 1))

    def test_get_other_teleporter(self):
        self.assertEqual(self.world.get_other_teleporter(1, 5), (8, 5))
        self.assertEqual(self.world.get_other_teleporter(8, 5), (1, 5))

    def test_break_obstacle(self):
        self.assertEqual(self.world.get_box(4, 6), "X")
        self.world.break_obstacle(4, 6)
        self.assertEqual(self.world.get_box(4, 6), " ")



if __name__ == '__main__':
    unittest.main()
