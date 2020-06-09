import csv
from winner import *

winners = []

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    for row in reader:
        current_winner = Winner(*row)
        winners.append(current_winner)


# 1. Create a list with all of the winners from the 1980s

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    eighties_movies = []
    for row in reader:
        if row[1][0:3] == "198":
            winner = Winner(*row)
            eighties_movies.append(winner)


print(eighties_movies)

# 2. Find the age of the oldest Oscar winner

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    oldest_age = 0
    for row in reader:
        winner = Winner(*row)
        if winner.age > oldest_age:
            oldest_age = winner.age

print(oldest_age)

# 3. Create a list with all of Meryl Streep's Oscar winning movies

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    find_movie_by_name = []
    for row in reader:
        winner = Winner(*row)
        if winner.name == "Meryl Streep":
            find_movie_by_name.append(winner.movie)

print(find_movie_by_name)
