class Winner:

    def __init__(self, index, year, age, name, movie):
        self.index = int(index)
        self.year = int(year)
        self.age = int(age)
        self.name = name
        self.movie = movie

    def values(self):
        return [self.index, self.year,
                self.age, self.name, self.movie]
