# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:18:08 2020

@author: aaron
"""



import cards
import pandas as pd


def load_data(input):
  for i, line in enumerate(input, 1):
    if line.startswith('#'):
      continue
    parts = line.strip().split('\t')
    if len(parts) != 2:
      raise IOError("wrong number of records on line %i" % (i))
    yield(parts)

if __name__ == "__main__":
  import datetime
  import argparse
  
  ap = argparse.ArgumentParser();
  ap.add_argument("-o", "--output", required=True, help="output file, usu example.cards")
  ap.add_argument("-x", "--excel_dataset", required=False,default = 'decks/temp.xlsx',
                  help="file with notecard data")
  
  args = vars(ap.parse_args())
  df = pd.read_excel('decks/temp.xlsx').to_dict()
  print(df)
  now = datetime.datetime.now()
  #not the same output File
  outputFile = open(args["output"], 'w')
  for column in df.keys():
      for key in df[column]:
          #print(key)
          #print(type(df[column][key]))
          print(str(key) + '\t' + str(df[column][key]), file = outputFile)
  
  inputFile = open(outputFile, 'r');
  outputFile = open(args["output"], 'w');
  #inputFile = open(args["tsv"], 'r')
  #outputFile = open(args["output"], 'w')
  cards.save(outputFile, (cards.card(top, bot, now) for top, bot in load_data(inputFile)))
  
