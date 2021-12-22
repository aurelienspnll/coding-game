import unittest
import robot

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.robot = robot.Robot(0, 0)

    def test_current_direction_index(self):
        self.assertEqual(self.robot.current_direction_index, 0)
        self.robot.increase_current_direction_index()
        self.assertEqual(self.robot.current_direction_index, 1)
        self.robot.increase_current_direction_index()
        self.assertEqual(self.robot.current_direction_index, 2)
        self.robot.reset_current_direction_index()
        self.assertEqual(self.robot.current_direction_index, 0)

    def test_get_opposite_direction(self):
        self.assertEqual(self.robot.get_opposite_direction("S"), "N")
        self.assertEqual(self.robot.get_opposite_direction("E"), "W")
        self.assertEqual(self.robot.get_opposite_direction("N"), "S")
        self.assertEqual(self.robot.get_opposite_direction("W"), "E")

    def test_get_current_direction_string(self):
        self.assertEqual(self.robot.get_current_direction_string(), "SOUTH")
        self.robot.set_current_direction("E")
        self.assertEqual(self.robot.get_current_direction_string(), "EAST")
        self.robot.set_current_direction("N")
        self.assertEqual(self.robot.get_current_direction_string(), "NORTH")
        self.robot.set_current_direction("W")
        self.assertEqual(self.robot.get_current_direction_string(), "WEST")

    def test_drink_beer(self):
        self.assertFalse(self.robot.is_drunk())
        self.robot.drink_beer()
        self.assertTrue(self.robot.is_drunk())
        self.robot.drink_beer()
        self.assertFalse(self.robot.is_drunk())

    def test_circuit_inverter(self):
        self.assertFalse(self.robot.is_invert())
        self.robot.circuit_inverter()
        self.assertTrue(self.robot.is_invert())
        self.robot.circuit_inverter()
        self.assertFalse(self.robot.is_invert())

    def test_change_direction(self):
        self.assertEqual(self.robot.get_current_direction(), "S")
        self.robot.change_direction()
        self.assertEqual(self.robot.get_current_direction(), "S")
        self.robot.increase_current_direction_index()
        self.robot.change_direction()
        self.assertEqual(self.robot.get_current_direction(), "E")
        self.robot.increase_current_direction_index()
        self.robot.change_direction()
        self.assertEqual(self.robot.get_current_direction(), "N")
        self.robot.increase_current_direction_index()
        self.robot.change_direction()
        self.assertEqual(self.robot.get_current_direction(), "W")
        self.robot.increase_current_direction_index()
        self.robot.change_direction()
        self.assertEqual(self.robot.get_current_direction(), "blocked")

    def test_move(self):
        self.assertEqual(self.robot.get_x(), 0)
        self.assertEqual(self.robot.get_y(), 0)
        self.robot.move(12, 9)
        self.assertEqual(self.robot.get_x(), 12)
        self.assertEqual(self.robot.get_y(), 9)
        self.assertEqual(self.robot.get_current_direction(), "S")
        self.assertEqual(self.robot.get_movement(), ["SOUTH"])
        self.robot.move(13, 8)
        self.assertEqual(self.robot.get_x(), 13)
        self.assertEqual(self.robot.get_y(), 8)
        self.assertEqual(self.robot.get_current_direction(), "S")
        self.assertEqual(self.robot.get_movement(), ["SOUTH", "SOUTH"])
        self.robot.set_current_direction("W")
        self.robot.move(15, 7)
        self.assertEqual(self.robot.get_x(), 15)
        self.assertEqual(self.robot.get_y(), 7)
        self.assertEqual(self.robot.get_current_direction(), "W")
        self.assertEqual(self.robot.get_movement(), ["SOUTH", "SOUTH", "WEST"])

    def test_clean_initial_direction_memory(self):
        self.robot.memory = ["S", "S", "S"]
        self.robot.clean_initial_direction_from_memory(2, "N")
        self.assertEqual(self.robot.memory, ["N", "N"])
        self.robot.clean_initial_direction_from_memory(2, "W")
        self.assertEqual(self.robot.memory, ["W", "W"])

    def test_is_stuck_in_loop(self):
        self.robot.memory = ["S", "S", "S"]
        self.robot.is_stuck_in_loop()
        self.assertFalse(self.robot.potential_loop)
        self.assertFalse(self.robot.is_looping())
        self.robot.memory = ["S", "W"]
        self.assertEqual("Memory is compromised...", self.robot.is_stuck_in_loop())
        self.assertFalse(self.robot.potential_loop)
        self.assertFalse(self.robot.is_looping())
        self.robot.memory = ["S", "S", "S", "N", "N"]
        self.robot.is_stuck_in_loop()
        self.assertFalse(self.robot.potential_loop)
        self.assertFalse(self.robot.is_looping())
        self.robot.memory = ["S", "S", "S", "N", "N", "N"]
        self.robot.is_stuck_in_loop()
        self.assertTrue(self.robot.potential_loop)
        self.assertFalse(self.robot.is_looping())
        self.assertEqual(self.robot.memory, ["N", "N", "N"])
        self.robot.memory = ["N", "N", "N", "S", "S", "S"]
        self.robot.is_stuck_in_loop()
        self.assertTrue(self.robot.potential_loop)
        self.assertTrue(self.robot.is_looping())

    def test_memorize_movement(self):
        self.assertEqual(self.robot.memory, [])
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["S"])
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["S", "S"])
        self.robot.set_current_direction("W")
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["W"])
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["W", "W"])
        self.robot.set_current_direction("E")
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["W", "W", "E"])
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["E", "E"])
        self.assertTrue(self.robot.potential_loop)
        self.assertFalse(self.robot.is_looping())
        self.robot.memorize_movement()
        self.assertEqual(self.robot.memory, ["E", "E", "E"])
        self.assertTrue(self.robot.potential_loop)
        self.assertFalse(self.robot.is_looping())
        self.robot.set_current_direction("W")
        self.robot.memorize_movement()
        self.robot.memorize_movement()
        self.robot.memorize_movement()
        self.assertTrue(self.robot.potential_loop)
        self.assertTrue(self.robot.is_looping())

if __name__ == '__main__':
    unittest.main()
