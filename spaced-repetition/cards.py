# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:59:47 2020

@author:
"""

"""
Flashcard data and operations.
"""

import datetime
import math
import random
import itertools

time_fmt = "%Y-%m-%d"

class card:
    #top = top string/data
    #bot = bot string/data
    #time = time of upcoming display in schedule
    #repetitions = number of times its been correctly answered in a row so far
    #interval = how long b/w upcoming and next time of display in days
    #easiness default to medium, 2.5
    #filename is where the individual card data can be stored
  def __init__(self, top, bot, time, repetitions=0, interval=1, easiness=2.5):
    self.top = top
    self.bot = bot
    self.time = time.replace(second=0, microsecond=0)
    self.repetitions = repetitions
    self.interval = interval
    self.easiness = easiness
    self.filename = None # Reserved for use by {load,save}_all

    #returns true if never come up previously
    #or if last time was answered wrong
  def is_new(self):
    return self.repetitions == 0

    #converts interval to days and adds it to time
  def next_time(self):
    return self.time + datetime.timedelta(days=math.ceil(self.interval))

    #THIS IS THE MAIN LOGIC/ALGORITHM!!!
    #quality of response
    #time displayed -> updates time attribute
  def repeat(self, quality, time):
    # SM-2 (name of algorithm)

    #quality of the response (accuracy)
    assert quality >= 0 and quality <= 5

    #update easiness based on quality
    self.easiness = max(1.3, self.easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02))

    if quality < 3: self.repetitions = 0
    #increment repeitition to keep track of number of times answered correctly in a row
    else: self.repetitions += 1

    #if only answered right once, repeat one day later
    if self.repetitions == 1: self.interval = 1

    #if twice in a row, repeat 6 days later (hardcoded)
    elif self.repetitions == 2: self.interval = 6

    #after twice, if super easy, interval greatly increases
    #if still hard, interval increases a little
    else: self.interval *= self.easiness
    self.time = time

    #seems like it just allows for cardA.is_new
    #instead of cardA.is_new()
  is_new = property(is_new)
  next_time = property(next_time)

#"saves" by printing the current state of cards and their attributes in an output file
def save(output, cards):
  for card in cards:
      #creates a tuple parts and prints it out
      #card time of upcoming display,  repeated correct responses,
      #interval til next display,  easiness
      #top data/string, bot data/string
      #printed with each attribute separated by a tab
    parts = (card.time.strftime(time_fmt), str(card.repetitions), str(card.interval), str(card.easiness), card.top, card.bot)
    print ('\t'.join(parts), file = output)

#loads data from an input file (counteracts save)
#a generator function -> generates cards, uses yield instead of return
def load(input):
  for line in input:
    parts = line.strip().split('\t')
    if len(parts) != 6:
        #then input format is invalid
      raise IOError("wrong number of records on line")
    time, repetitions, interval, easiness, top, bot = parts
    time = datetime.datetime.strptime(time, time_fmt)
    repetitions = int(repetitions)
    interval = float(interval)
    easiness = float(easiness)
    new = card(top, bot, time, repetitions, interval, easiness)
    #basically returns new cards one by one in a sequence
    yield new


#saves the statae of each card in their filename attribute's file
#contrast with save which stores it all in one file
def save_all(cards):
  outputs = {}
  try:
    for card in cards:
      if card.filename not in outputs:
        outputs[card.filename] = open(card.filename, 'w')
      save(outputs[card.filename], [card])
  finally:
    for output in outputs.values():
      output.close()

#loads from each individual filename of each card
#still a generator function
def load_all(filenames):
  for filename in filenames:
    with open(filename) as input:
      for card in load(input):
        card.filename = filename
        yield card

#returns two functions!!!!
#choose next and reject card
def fetch_cards(cards, now, max_reviews=None, max_new=None, randomize=False):
  #extracts new cards from list of cards
  #FIFO
  new_cards = list(itertools.islice((c for c in cards if c.is_new), max_new))
  new_cards.reverse()

  #answered questions (time < now);
  #FIFO
  to_review = list(itertools.islice((c for c in cards if not c.is_new and c.next_time <= now), max_reviews))
  to_review.reverse()

  #then not FIFO, instead random order of review
  if randomize:
    random.shuffle(to_review)

    #treats to_review and new_cards as stacks
    #finishes review first
    #then uses the new_cards stack
  def choose_next():
    if len(to_review) > 0:
      return to_review.pop()
    elif len(new_cards) > 0:
      return new_cards.pop()
    else:
      return None

    #takes a new card
    #if its new add to new card stack
    #if not add to to_review
  def reject_card(card):
    if card.is_new:
      new_cards.insert(0, card)
    else:
      to_review.insert(0, card)
  return choose_next, reject_card


#basically after lots of input either reviews it
def run_cards(cards, now, review_card, max_reviews=None, max_new=None, randomize=False):
  choose_next, reject_card = fetch_cards(cards, now, max_reviews, max_new, randomize)

  while True:
    current = choose_next()

    #if finished with everything
    if current is None:
      break
    quality = review_card(current)

    #basically updtes each card's schedule
    current.repeat(quality, now)

    #calls reject_card to tell how to process it and which stack to add to
    if current.is_new:
      reject_card(current)

def bulk_review(cards, now, batch_size, show_batch, review_card, max_reviews=None, max_new=None, randomize=False):
  import random

  choose_next, reject_card = fetch_cards(cards, now, max_reviews, max_new, randomize)

  batch = [n for i in range(batch_size) for n in [choose_next()] if n is not None]
  while len(batch) > 0:
    random.shuffle(batch)

    show_batch(batch)
    def run_card(card):
      quality = review_card(card)
      card.repeat(quality, now)
      return quality
    batch = [c for c in batch for r in [run_card(c)] if c.is_new]

    while len(batch) < batch_size:
      next = choose_next()
      if next is None:
        break
      batch.append(next)
