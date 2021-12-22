import unittest
import engine
import world
import robot

"""
World definiton:
##########
#    T   #
#        #
#        #
#     X  #
#@BI  X  #
#     X  #
#        #
#    T  $#
##########
"""

class TestUtils(unittest.TestCase):
    def setUp(self):
        world_def = "###########    T   ##        ##        ##     X  ##@BI  X  ##     X  ##        ##    T  $###########"
        self.world = world.World(10, 10, world_def)
        self.robot = robot.Robot(5, 1)
        self.engine = engine.Engine(self.robot, self.world)

    def test_next_robot_pos(self):
        self.assertEqual(self.engine.next_robot_pos(), (6, 1))
        self.robot.set_current_direction("E")
        self.assertEqual(self.engine.next_robot_pos(), (5, 2))
        self.robot.set_current_direction("N")
        self.assertEqual(self.engine.next_robot_pos(), (4, 1))
        self.robot.set_current_direction("W")
        self.assertEqual(self.engine.next_robot_pos(), (5, 0))

    def test_move_robot(self):
        # case : #
        self.assertFalse(self.engine.move_robot(0, 0))
        self.assertEqual(self.engine.robot.get_x(), 5)
        self.assertEqual(self.engine.robot.get_y(), 1)
        # case : @
        self.assertTrue(self.engine.move_robot(5, 1))
        self.assertEqual(self.engine.robot.get_x(), 5)
        self.assertEqual(self.engine.robot.get_y(), 1)

        # case : X when robot is not drunk
        self.assertFalse(self.engine.move_robot(4, 6))
        self.assertEqual(self.engine.world.get_box(4, 6), "X")

        # case : B
        self.assertTrue(self.engine.move_robot(5, 2))
        self.assertTrue(self.engine.robot.is_drunk())
        self.assertEqual(self.engine.robot.get_x(), 5)
        self.assertEqual(self.engine.robot.get_y(), 2)

        # case : X when robot is drunk
        self.assertTrue(self.engine.move_robot(4, 6))
        self.assertEqual(self.engine.robot.get_x(), 4)
        self.assertEqual(self.engine.robot.get_y(), 6)
        self.assertEqual(self.engine.world.get_box(4, 6), " ")

        # case : B when robot is drunk
        self.assertTrue(self.engine.move_robot(5, 2))
        self.assertFalse(self.engine.robot.is_drunk())
        self.assertEqual(self.engine.robot.get_x(), 5)
        self.assertEqual(self.engine.robot.get_y(), 2)

        # case : I
        self.assertTrue(self.engine.move_robot(5, 3))
        self.assertTrue(self.engine.robot.is_invert())
        self.assertEqual(self.engine.robot.get_x(), 5)
        self.assertEqual(self.engine.robot.get_y(), 3)

        # case : I when robot is inverted
        self.assertTrue(self.engine.move_robot(5, 3))
        self.assertFalse(self.engine.robot.is_invert())
        self.assertEqual(self.engine.robot.get_x(), 5)
        self.assertEqual(self.engine.robot.get_y(), 3)

        # case : T
        self.assertTrue(self.engine.move_robot(1, 5))
        self.assertEqual(self.engine.robot.get_x(), 8)
        self.assertEqual(self.engine.robot.get_y(), 5)

        # case : " "
        self.assertTrue(self.engine.move_robot(3, 3))
        self.assertEqual(self.engine.robot.get_x(), 3)
        self.assertEqual(self.engine.robot.get_y(), 3)
        
        # case : $
        self.assertTrue(self.engine.move_robot(8, 8))
        self.assertTrue(self.engine.arrived)


if __name__ == '__main__':
    unittest.main()