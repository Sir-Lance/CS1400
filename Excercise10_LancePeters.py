#Lance Peters
#CS1400
#MrAbrahasmTeng
#Excercise10

import csv

with open('station.csv') as f:
#part 1
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
    print("station_filtered.csv ...saved")
else:
    print("file not saved...")

#part 2
list2 = []
with open('station_filtered.csv') as d:
    filtered = list(csv.reader(d))
    for field in filtered:
        list2.extend(field)
        list2.pop(0)
        list2 = [float(i) for i in list2]
print(list2)

hanzo_got_nerfed = (sum(list2[:]))/len(list2)
print(hanzo_got_nerfed)

answer2 = input("Output to .txt? y or n?")
if answer2 == "y":
    output = open("drainage-area-avg.txt","w")
    genji_needs_a_buff = str(hanzo_got_nerfed)
    output.write(genji_needs_a_buff)
else:
    print("skipped...")
#part 3 (encode)
genji_needs_a_buff = str(hanzo_got_nerfed)
answer3 = input("Encode drainage-area.txt? y or n?")
if answer3 == "y":
    output2 = open("drainage-area-avg.txt", "r")
    temp = []
    for character in genji_needs_a_buff:
        temp.append(ord(character)+3)
        yeet = open("fileciphertext.txt", "w")
        yeet.write(str(temp))
