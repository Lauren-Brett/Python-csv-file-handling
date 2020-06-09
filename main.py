import csv
from winner import *

winners = []

# --- "with" is for file handling
#  it will open it and then close it,
# --- "open" takes in parameters,
# -- "r" = mode of opening it - so "r" = "read"
# -- "as" = we can reference the file as ...

# with open("oscars.csv", "r") as banana:
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    # -- next here will skip the first row in the file as we dont want this to be read as "index" is not an int
    next(reader)
    for row in reader:
        # current_winner = Winner(row[0], row[1], row[4])
        current_winner = Winner(*row)
        winners.append(current_winner)

# ---- 1
# with open("oscars.csv", "r") as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     count = sum(1 for row in reader)

# # -- "a" append mode
# with open("oscars.csv", "a") as csvfile:
#     # -- all colums have all values properly quoted
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#     winner = Winner(count, 2020, 50, "Renee Zellweger", "Judy")
#     writer.writerow(winner.values())


# ----- 2
# -- "w" write mode
with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

    for winner in winners:
        if winner.year == 2020:
            winner.age += 1
        writer.writerow(winner.values())


for winner in winners:
    print(f"{winner.name} won the oscar for {winner.movie} in {winner.year} aged {winner.age}")
