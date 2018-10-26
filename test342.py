import csv

with open('station.csv') as f:

    reader = csv.reader(f)

    user_list = []
    for row in reader:
        if any(row[7]):
            print (row[7])
            user_list.append(row[7])

answer = input("Save CSV - y or n?")
if answer == "y":
    out = csv.writer(open("station_filtered.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(user_list)
    print("station_filtered.csv ---saved")
else:
    print("file not saved")

txtout = writer(station)
