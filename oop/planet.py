from human import Human
from robot import Robot


class Planet:
    def __init__(self):
        self.inhabitants = {'humans': [], 'robots': []}

    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        self.inhabitants['robots'].remove(robot)


if __name__ == "__main__":
    planet = Planet
    sam = Human("Sam")
    planet.add_human(sam)
    print(planet)
