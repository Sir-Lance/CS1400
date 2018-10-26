fName = open("test.txt", "r")
#r = read / read data from file.
#w = write / write data to a file.
#a = append / update existing file.
type(fName)
data = fName.read()
fName.close()
line = fName.readline()
#reads first readline
dataField = line.split(",")
#the information stored is pulled as a string and can be manipulatedself.
dataField[10]
int(dataField[4])
lines = fName.readlines()
