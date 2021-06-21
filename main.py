import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imgName = "TextDocument.png"
img = cv2.imread(imgName)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

string = ""
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b[0],end="")

    #string = string + b
    b = b.split(' ')
    #print(b)
    
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    
    #This is for putting rectangle box 
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 1)

    #This is also for putting text over the box
    #cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


# cv2.imshow('img', img)
# cv2.waitKey(0)

string = pytesseract.image_to_string(img)
print(string)
with open("string.txt",'w') as f:
    f.write(string)
cv2.imshow('img', img)
cv2.waitKey(0)