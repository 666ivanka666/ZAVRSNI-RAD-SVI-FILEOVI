from PIL import Image
from math import sqrt


imag = Image.open("slika_1.jpg")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')
#coordinates of the pixel
X,Y = 0,0
#Get RGB
pixelRGB = imag.getpixel((X,Y))
R,G,B = pixelRGB 
brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)
print(brightness)
