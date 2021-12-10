class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"human name = {self.name}, age = {self.age}, energy = {self.energy}"

    def __str__(self):
        return f"Human {self.name} is {self.age} years old and has {self.energy} energy"

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if amount + self.energy < 101:
            self.energy += amount
        else:
            self.energy = self.MAX_ENERGY

    def move(self, distance):
        if self.energy - distance > 0:
            self.energy = self.energy - distance
        else:
            self.energy = 0


if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
    print(human)
