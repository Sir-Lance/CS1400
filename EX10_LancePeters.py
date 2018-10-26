import csv

file = open('station.csv')
csv_file = csv.reader(file)

for row in csv_file:
    print(row[7])
    if not ''.join(row).strip():
