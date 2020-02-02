# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:39:23 2020

@author: aaron
"""
import cards
import argparse
import datetime

def review_c(card):
    print("Question: define this and give pinyin   " + card.top)
    print(" ")
    answer = input()
    print ("Answer: " + card.bot)
    print("How well did you do? 1-5")
    return int(input())
    #return answer == card.bot#round(random.random())
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cards", required=True, help = "file containing cards, formated with time and easiness, etc")
args = vars(ap.parse_args())

deck = (cards.load(open(args["cards"], 'r')))

cards.run_cards(deck, datetime.datetime.now(),
                review_c)
print(deck)