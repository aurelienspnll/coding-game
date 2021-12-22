import robot
import world

class Engine:
    def __init__(self, robot, world):
        self.robot = robot
        self.world = world
        self.arrived = False
        self.turn = 0

    def print_world_and_robot(self):
        for i in range(self.world.get_height()):
            line = ""
            for j in range(self.world.get_width()):
                if i == self.robot.get_x() and j == self.robot.get_y():
                    line += "R"
                else: 
                    line += self.world.get_box(i, j)
            print(line)

    def next_robot_pos(self):
        if self.robot.get_current_direction() == "S":
            return self.robot.get_x()+1, self.robot.get_y()
        elif self.robot.get_current_direction() == "E":
            return self.robot.get_x(), self.robot.get_y()+1
        elif self.robot.get_current_direction() == "N":
            return self.robot.get_x()-1, self.robot.get_y()
        elif self.robot.get_current_direction() == "W":
            return self.robot.get_x(), self.robot.get_y()-1
        else:
            return -1, -1

    def move_robot(self, next_x, next_y):
        next_box = self.world.get_box(next_x, next_y)
        if next_box == "#":
            return False
        elif next_box == "X":
            if self.robot.is_drunk():
                self.robot.move(next_x, next_y)
                self.world.break_obstacle(next_x, next_y)
                return True
            else:
                return False
        elif next_box == "@":
            self.robot.move(next_x, next_y)
            return True
        elif next_box == "$":
            self.robot.move(next_x, next_y)
            self.arrived = True
            return True
        elif next_box == "S" or next_box == "E" or next_box == "N" or next_box == "W":
            self.robot.move(next_x, next_y)
            self.robot.set_current_direction(self.world.get_box(next_x, next_y))
            return True
        elif next_box == "B":
            self.robot.move(next_x, next_y)
            self.robot.drink_beer()
            return True
        elif next_box == "I":
            self.robot.move(next_x, next_y)
            self.robot.circuit_inverter()
            return True
        elif next_box == "T":
            x, y = self.world.get_other_teleporter(next_x, next_y)
            self.robot.move(x, y)
            return True
        elif next_box == " ":
            self.robot.move(next_x, next_y)
            return True
        else: # propably an error
            return False

    def play(self):
        while not(self.arrived):
            self.turn += 1
            x, y = self.next_robot_pos()
            if x == -1 and y == -1:
                return # error
            else:
                has_moved = self.move_robot(x, y)
                if not(has_moved):
                    self.robot.change_direction()
                    self.robot.increase_current_direction_index()
                else:
                    self.print_world_and_robot()
                    self.robot.reset_current_direction_index()
                    if self.robot.is_looping():
                        print("LOOP")
                        return
        for move in self.robot.get_movement():
            print(move)
        return 