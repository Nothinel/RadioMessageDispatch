#!/bin/python

"""
This will create a set of documents for playing my funkspiel, one for each
player, soon this should get data from a config file to determine what to do
"""

number_of_players = 1

with open("doc_template.tex", "r") as f:
    full_string = f.read()
print(full_string)
