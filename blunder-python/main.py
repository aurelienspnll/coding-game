import robot
import engine
import world
import sys

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    # lines = f.r
    first_line = f.readline().split()
    l, c = first_line[0], first_line[1]
    world_def = ""
    for line in f.readlines():
        world_def += line.replace('\n', '')
    w = world.World(l, c, world_def)
    x, y = w.get_start_position()
    r = robot.Robot(x, y)
    e = engine.Engine(r, w)
    e.play()