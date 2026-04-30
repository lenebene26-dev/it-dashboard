class Zookeeper:
    """Represents a zookeeper assigned to habitats."""

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.assigned_habitats = []

    def assign(self, habitat):
        """Assigns a habitat to the zookeeper."""
        self.assigned_habitats.append(habitat)

    def daily_report(self):
        """Prints the zookeeper daily report."""
        print(f"Keeper: {self.name} ({self.specialty})")

        for habitat in self.assigned_habitats:
            print(f"  {habitat}")

            for animal in habitat.animals:
                print(f"    {animal.describe()}")