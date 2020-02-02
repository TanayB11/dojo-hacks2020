# -*- coding: utf-8 -*-
"""
NAME
----
fulgurate-import - convert a two-column TSV file to a flashcard file
SYNOPSIS
--------
*fulgurate-import* ['OPTIONS'] TSV-FILE [CARDS-FILE]
DESCRIPTION
-----------

"""

import cards

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
  #import getopt
  import argparse
  
  ap = argparse.ArgumentParser();
  ap.add_argument("-t", "--tsv", required=True, help="file with notecard data")
  ap.add_argument("-o", "--output", required=True, help="output file, usu example.cards")
  args = vars(ap.parse_args())
  now = datetime.datetime.now()
  
  inputFile = open(args["tsv"], 'r')
  outputFile = open(args["output"], 'w')
  cards.save(outputFile, (cards.card(top, bot, now) for top, bot in load_data(inputFile)))
  
