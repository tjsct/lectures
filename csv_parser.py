import csv

FNAME = "List of all lectures (for website) - Lectures.csv"

with open(FNAME) as f:
    reader = csv.reader(f, delimiter=",")
    data = [row for row in reader]

l = []
for row in data:
    # do something with data
data = l

with open(FNAME, "w") as f:
    writer = csv.writer(f, delimiter=",")
    for row in data:
        writer.writerow(row)

