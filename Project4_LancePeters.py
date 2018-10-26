import math

month = int(input("Months: ")) + 1
adult = 1
babies = 0
#total = adult + babies
print("Month\t Adult\t Babies\t Total")

for i in range(month):
    anime = babies + i
    for j in range(month):
          yeet = adult * anime
    total = anime + yeet
    print(i, '\t', yeet, '\t', anime, '\t', total)
    if total >= 501:
        print("Room full - Exceeds 500")
        print("It will take ", i, "months to fill up the cages.")
        break
