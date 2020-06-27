#!/bin/python3

"""
This will create a set of documents for playing my funkspiel, one for each
player, soon this should get data from a config file to determine what to do
"""
import json
import glob
import random
class Player:
    pass

#create a few global parameters, to be set before creating a game
number_of_players = 2
number_of_tasks_per_player = 2

#organize some things or create data structures according to the parameters set above
list_players = []
for i in range(0, number_of_players):
    player = Player()
    list_players.append(player)
    player.number=i
    player.tasks = []

print(list_players[0].number)

number_of_tasks = number_of_players * number_of_tasks_per_player
tasks_folder = "Tasks/Test/"
list_task_files = glob.glob(tasks_folder + "*.json")
list_tasks = []
for task_file in list_task_files:
    with open(task_file, "r") as f:
        task = json.load(f)
        list_tasks.append(task)

#randomly assign the tasks to players
list_tasks = random.sample(list_tasks, number_of_tasks)

for player in list_players:
    pass

print(task)

#with open("doc_template.tex", "r") as f:
    #full_string = f.read()
#print(full_string)
