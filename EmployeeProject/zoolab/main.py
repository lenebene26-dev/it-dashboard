from animal import Dog, Bird, Fish
from habitat import Habitat
from zoo import Zoo
from zookeeper import Zookeeper


def main():
    """Runs the zoo lab program."""

    dog = Dog("Rex", "Canine", "German Shepherd")
    bird1 = Bird("Tweety", "Avian", True)
    bird2 = Bird("Penguin Pete", "Avian", False)
    fish = Fish("Nemo", "Fish", "saltwater")

    savanna = Habitat("Savanna Exhibit", "tropical", 5)
    aviary = Habitat("Sky Dome Aviary", "temperate", 10)
    aquarium = Habitat("Deep Blue Aquarium", "aquatic", 20)

    print(savanna.add_animal(dog))
    print(aviary.add_animal(bird1))
    print(aviary.add_animal(bird2))
    print(aquarium.add_animal(fish))
    print()

    zoo = Zoo("Delena's Wildlife Park")
    zoo.add_habitat(savanna)
    zoo.add_habitat(aviary)
    zoo.add_habitat(aquarium)

    keeper = Zookeeper("Sara", "Birds")
    keeper.assign(aviary)

    zoo.hire_keeper(keeper)

    zoo.full_report()
    keeper.daily_report()


if __name__ == "__main__":
    main()