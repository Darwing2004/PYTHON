# Write code below 💖


class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


Paris = City("Paris", "France", 68000000, "Eiffel Tower")
New_York = City("New York", "USA", 700000000, "Apple Town")

print(vars(Paris))
print(vars(New_York))
