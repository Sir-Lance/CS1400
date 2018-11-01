#Lance Peters
#CS1400
#MrAbrahamTeng
#Exercise11
dictvar = dict()
file = open("world-cities-population.csv","r" ,encoding="utf8")
linepos = 0
for line in file:
    linepos = linepos + 1
    line = line.rstrip()
    temp = line.split(',')
    dictvar[temp[0]] = (temp[4], temp[9])
    if linepos == 647:
        break

print(dictvar)
select = input("Type Country Name: ")
print(dictvar.get(select))
#Where is North American data in the CSV?
#any way the program works and you can have it pull specific data
#by typing in the country name.
