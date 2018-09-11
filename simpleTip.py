#Lance Peters, CS1400-003, 9/8/2018
#Create a program that calculates total and tip total
#I created a simple set of variables for each service tier to call upon

import math

#Input price of meal
price = float(input("What was the total bill: $"))
#Variables to calculate tip
excellent = (price * 0.20)
average = (price * 0.15)
poor = (price * 0.10)


print(f"Bill total: ${price:,.2f}")
print("How was your service today?")
print("1. Excellent, 2. Average, or 3. Poor?")
#not required but a line to define what kind of service you got
service = input("excellent, average, poor?: ")

if(service == "excellent"):
    print(f"Tip ${excellent:,.2f}")
if(service == "average"):
    print(f"Tip ${average:,.2f}")
if(service == "poor"):
     print(f"Tip ${poor:,.2f}")


#----------fulltext output CS1400----------
print(" ")
print("---Required CS1400 Output---")
print(f"Enter the cost of the meal: ${price:,.2f}")
print(f"Cost of meal: ${price:,.2f}")
print(f"Excellent Service tip: ${excellent:,.2f} total: ${excellent + price:,.2f}")
print(f"Average Service tip: ${average:,.2f} total: ${average + price:,.2f}")
print(f"Poor Service tip: ${poor:,.2f} total: ${poor + price:,.2f}")

#I learned how to format and make the code look nice
#It was difficult remembering how to format to the second decimal on each output
