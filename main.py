import main
import cv2 as cv
import numpy as np
from os import system
from time import sleep

from pip import main

print(" BASIC OPERATIONS ON IMAGES")
system('cls')
img = cv.imread('dubu.jpg')
print(img.shape)
if len(img.shape) == 3:
    s = img.shape
    x = int(input("\nEnter 'x' coordinate value (max value "+str(s[0])+" ) : "))
    y = int(input("Enter 'y' coordinate value (max value "+str(s[1])+" ) : "))
    bgr = int(input("""CHOOSE :\n0 - blue\n1 - green\n2 - red\n--> """))
    print("Pixel value: ", img.item(x,y,bgr))
    sleep(5)
    print("Modifying a pixel")
    x = int(input("Enter 'x' coordinate value (max value "+str(s[0])+" ) : "))
    y = int(input("Enter 'y' coordinate value (max value "+str(s[1])+" ) : "))
    bgr = int(input("""CHOOSE :\n0 - blue\n1 - green\n2 - red\n--> """))
    print("Current value: ", img.item(x,y,bgr))
    new=int(input("Enter new value: "))
    img.itemset((x,y,bgr),new)
    print("New value: ", img.item(x,y,bgr))
    sleep(5)
    s_new = []
    x_new = int(input("Enter desired Width in pixel: "))
    y_new = int(input("Enter desired Height in pixel: "))
    #checking
    #cheking:
    if x_new <= s[0] and y_new <= s[1]:
        print(str(x_new) +"," + str(y_new) + " is in the image dimension which is " + str(s[0]) + "," + str(s[1]))
        sleep(3)
        pix = 10000
        image_size = img.size
        if pix <= image_size:
            print("The set image pixel count (pix =" + str(pix) + ") is in the bounderies of the original image ( " + str(image_size))
            sleep(2)
            print("The image is in data type " + str(img.dtype))
            sleep(100)
        else:
            print("The set image pixel count (pix =" + str(pix) + ") is not in the bounderies of the original image ( " + str(image_size))
            sleep(3)
    else:
        print("Not in the boundery of " + str(s[0]) +"," + str(s[1]))
        sleep(3)
else:
    print("Image is grayscale!\nUse another image!")
    sleep(3)
    main
