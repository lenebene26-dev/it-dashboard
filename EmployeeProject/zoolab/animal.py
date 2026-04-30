from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    """Dog subclass."""

    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def move(self):
        return "runs on four legs"


class Bird(Animal):
    """Bird subclass."""

    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly

    def speak(self):
        return "Chirp!"

    def move(self):
        if self.can_fly:
            return "flies through the air"
        else:
            return "walks and waddles"


class Fish(Animal):
    """Fish subclass."""

    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type

    def speak(self):
        return "Blub!"

    def move(self):
        return "swims through the water"