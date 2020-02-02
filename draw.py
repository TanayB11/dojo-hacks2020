# https://www.life2coding.com/paint-opencv-images-save-image/
import cv2
import numpy as np

drawing=False
mode=True
# mouse callback function
def paint_draw(event,former_x,former_y,flags,param):
    global current_former_x,current_former_y,drawing, mode
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        current_former_x,current_former_y=former_x,former_y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.line(image,(current_former_x,current_former_y),(former_x,former_y),(0,0,0),10) #232, 239, 250
                current_former_x = former_x
                current_former_y = former_y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.line(image,(current_former_x,current_former_y),(former_x,former_y),(0,0,0),10)
            current_former_x = former_x
            current_former_y = former_y
    return former_x,former_y


image = cv2.imread("background.png")
cv2.resize(image, (250, 250))
cv2.namedWindow("OpenCV Paint Brush")
cv2.setMouseCallback('OpenCV Paint Brush',paint_draw)
while(1):
    cv2.imshow('OpenCV Paint Brush',image)
    k=cv2.waitKey(1)& 0xFF
    if k==32: #space KEY
        cv2.imwrite("image.png",image)
        break
cv2.destroyAllWindows()
