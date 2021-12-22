class Robot:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.invert = False
        self.drunk = False
        self.current_direction = "S"
        self.direction = ["S", "E", "N", "W"]
        self.current_direction_index = 0
        self.potential_loop = False
        self.loop = False
        self.memory = []
        self.movement = []

    def move(self, x, y):
        self.x = x
        self.y = y
        self.movement.append(self.get_current_direction_string())
        self.memorize_movement()
    
    def get_opposite_direction(self, direction):
        if direction == "S":
            return "N"
        elif direction == "E":
            return "W"
        elif direction == "N":
            return "S"
        elif direction == "W":
            return "E"

    def memorize_movement(self):
        if len(self.memory) == 0:
            self.memory.append(self.current_direction)
        else:
            if self.memory[0] == self.current_direction: # The robot continues his path
                self.memory.append(self.current_direction)
            elif self.memory[0] == self.get_opposite_direction(self.current_direction): # The robot comes back
                self.memory.append(self.current_direction)
                self.is_stuck_in_loop()
            else: # The robot can't be in loop in this case
                self.memory = []
                self.potential_loop = False # Reset
                self.memory.append(self.current_direction) # It starts his new journey

    def clean_initial_direction_from_memory(self, opposite_direction_count, opposite_direction):
        self.memory = []
        for i in range(opposite_direction_count):
            self.memory.append(opposite_direction)

    def is_stuck_in_loop(self):
        initial_direction = self.memory[0]
        initial_direction_count = 0
        opposite_direction = self.get_opposite_direction(initial_direction)
        opposite_direction_count = 0
        for move in self.memory:
            if move == initial_direction:
                initial_direction_count += 1
            elif move == opposite_direction:
                opposite_direction_count += 1
            else:
                return "Memory is compromised..."
        if initial_direction_count == opposite_direction_count:
            if self.potential_loop:
                self.loop = True
            else:
                self.potential_loop = True
                self.clean_initial_direction_from_memory(opposite_direction_count, opposite_direction)
    
    def get_current_direction_string(self):
        if self.current_direction == "S":
            return "SOUTH"
        elif self.current_direction == "E":
            return "EAST"
        elif self.current_direction == "N":
            return "NORTH"
        elif self.current_direction == "W":
            return "WEST"
    
    def change_direction(self):
        if self.current_direction_index >= 0 and self.current_direction_index < len(self.direction):
            if self.invert:
                self.current_direction = self.direction[len(self.direction)-(self.current_direction_index+1)]
            else:
                self.current_direction = self.direction[self.current_direction_index]
        else:
            self.current_direction = "blocked"
    
    def increase_current_direction_index(self):
        self.current_direction_index += 1

    def reset_current_direction_index(self):
        self.current_direction_index = 0
    
    def set_current_direction(self, direction):
        self.current_direction = direction

    def get_current_direction(self):
        return self.current_direction

    def get_movement(self):
        return self.movement

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_invert(self):
        return self.invert

    def is_drunk(self):
        return self.drunk
    
    def drink_beer(self):
        self.drunk = not(self.drunk)

    def circuit_inverter(self):
        self.invert = not(self.invert)

    def is_looping(self):
        return self.loop
