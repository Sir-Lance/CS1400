from PIL import Image
myImg = Image.open('Image1.jpg')
newImg = myImg.convert('L')
print("Do you want your ", myImg, "converted to GRY?")
print("Type: y or n")
answer = str(input("y or n?: "))
if answer == "y":
    newImg.show()
    newImg.save('Image1_Grayscale.jpg')
if answer == "n":
    myImg.show()
