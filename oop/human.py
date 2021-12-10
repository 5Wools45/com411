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


if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
    print(human)
