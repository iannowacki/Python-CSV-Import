import csv

with open("CSVfile.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row[""])
