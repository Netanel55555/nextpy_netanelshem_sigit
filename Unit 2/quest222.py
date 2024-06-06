class Turtle:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 0
        Turtle.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    first_turtle = Turtle("poofi")
    second_turtle = Turtle()

    first_turtle.birthday()

    print(first_turtle.get_name())
    print(second_turtle.get_name())

    second_turtle.set_name("boofi")
    print(second_turtle.get_name())

    print(Turtle.count_animals)



