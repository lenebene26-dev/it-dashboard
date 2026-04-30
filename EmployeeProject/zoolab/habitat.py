class Habitat:
    """Represents a habitat that contains animals."""

    def __init__(self, name, climate, capacity):
        self.name = name
        self.climate = climate
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        """Adds an animal if the habitat is not full."""
        if len(self.animals) >= self.capacity:
            return f"{self.name} is full. Could not add {animal.name}."

        self.animals.append(animal)
        return f"{animal.name} was added to {self.name}."

    def roll_call(self):
        """Prints all animals in the habitat."""
        for animal in self.animals:
            print(f"  {animal.describe()}")
            print(f"    Sound: {animal.speak()}")
            print(f"    Movement: {animal.move()}")

    def __str__(self):
        return f"[{self.climate}] {self.name} ({len(self.animals)}/{self.capacity})"