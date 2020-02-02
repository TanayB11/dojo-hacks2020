# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:39:23 2020

@author: aaron
"""
import cards
import argparse
import datetime, cv2
import predict, time, os
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
                cv2.line(image,(current_former_x,current_former_y),(former_x,former_y),(0,0,0),15) #232, 239, 250
                current_former_x = former_x
                current_former_y = former_y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.line(image,(current_former_x,current_former_y),(former_x,former_y),(0,0,0),15)
            current_former_x = former_x
            current_former_y = former_y
    return former_x,former_y

def get_img():
    # Displaying the image
    cv2.resize(image, (250, 250))
    cv2.namedWindow('hi')
    cv2.setMouseCallback('hi',paint_draw)
    while(1):
        cv2.imshow('hi',image)
        k=cv2.waitKey(1)
        if k==32: #space KEY
            cv2.imwrite("image.png",image)
            cv2.destroyAllWindows()
            break

def review_c(card):
    print("Write: " + card.bot)
    get_img()
    # os.system('clear')
    answer = predict.prediction()
    if (answer==card.top):
        print('CORRECT!')
        return 5
    else:
        return 1

os.system('clear')
image = cv2.imread("background.png")


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cards", required=True, help = "file containing cards, formated with time and easiness, etc")
args = vars(ap.parse_args())

deck = (cards.load(open(args["cards"], 'r')))

cards.run_cards(deck, datetime.datetime.now(),
                review_c)
print(deck)
