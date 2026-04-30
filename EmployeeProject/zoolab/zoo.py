class Zoo:
    """Represents a zoo with habitats and zookeepers."""

    def __init__(self, name):
        self.name = name
        self.habitats = []
        self.keepers = []

    def add_habitat(self, habitat):
        """Adds a habitat to the zoo."""
        self.habitats.append(habitat)

    def hire_keeper(self, keeper):
        """Adds a zookeeper to the zoo."""
        self.keepers.append(keeper)

    def total_animals(self):
        """Returns total animals across all habitats."""
        total = 0

        for habitat in self.habitats:
            total += len(habitat.animals)

        return total

    def full_report(self):
        """Prints a full zoo report."""
        print(f"=== {self.name} ===")
        print("Student: Delena Davis")
        print(f"Habitats: {len(self.habitats)}")
        print(f"Animals: {self.total_animals()}")
        print(f"Keepers: {len(self.keepers)}")
        print()

        for habitat in self.habitats:
            print(habitat)
            habitat.roll_call()
            print()