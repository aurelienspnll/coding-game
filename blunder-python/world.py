class World:
    def __init__(self, height, width, world_definition):
        self.height = int(height)
        self.width = int(width)
        self.tab = []
        for c in world_definition:
            self.tab.append(c)

    def print_world(self):
        for i in range(self.height):
            line = ""
            for j in range(self.width):
                line += self.tab[i*self.width+j]
            print(line)

    def get_start_position(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.tab[i*self.width+j] == "@":
                    return i, j
        return -1, -1

    def get_other_teleporter(self, x, y):
        for i in range(self.height):
            for j in range(self.width):
                if self.tab[i*self.width+j] == "T" and (i != x or j != y):
                    return i, j
        return -1, -1

    def break_obstacle(self, x, y):
        self.tab[x*self.width+y] = " "
    
    def get_box(self, x, y):
        return self.tab[x*self.width+y]
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width

    def get_tab(self):
        return self.tab