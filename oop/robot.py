class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")


if __name__ == "__main__":
    robot = Robot()
    robot.display()
