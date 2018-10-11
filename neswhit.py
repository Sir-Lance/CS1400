name = input("Namae Wa? ")
#name = name.lower()
output = []
for character in name:
    number = (ord(character) - 96)
    output.append(number)
print(output)
