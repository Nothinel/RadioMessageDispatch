#!/usr/bin/python3

"""
This will create a set of documents for playing my funkspiel, one for each
player, soon this should get data from a config file to determine what to do
"""
import json
import glob
import random
import maketasks
class Player:
    pass

def read_tasks(folder):
    list_task_files = glob.glob(folder + "*.json")
    list_tasks = []
    for task_file in list_task_files:
        with open(task_file, "r") as f:
            task = json.load(f)
            list_tasks.append(task)
    return list_tasks
    
def player_tasks2latex_str(player):
    latex_str = ""
    #print(player.tasks)
    for task in player.tasks:
        #print(task)
        latex_str += f"\\subsection{{TaskID: {task['task_id']}}}\n"
        latex_str += f"\\textbf{{Aufgabenstellung}}: "
        latex_str += f"{task['assignment']}"
    return latex_str
    

#create a few global parameters, to be set before creating a game
number_of_players = 3
number_of_tasks_per_player = 20

#organize some things or create data structures according to the parameters set above
list_players = []
for i in range(0, number_of_players):
    player = Player()
    list_players.append(player)
    player.number=i
    player.tasks = []

#print(list_players[0].number)

number_of_tasks = number_of_players * number_of_tasks_per_player
tasks_folder = "Tasks/Test/"
list_tasks = read_tasks(tasks_folder)
#randomly assign the tasks to players
list_tasks = random.sample(list_tasks, number_of_tasks)
random.shuffle(list_tasks)
#list_tasks = list(range(0,len(list_tasks)))
#print(list_tasks)
for player in list_players:
    start = player.number*number_of_tasks_per_player
    stopp = (player.number+1)*number_of_tasks_per_player 
    #print(f"{start}   {stopp}")
    #print(list_tasks[start:stopp])
    player.tasks += list_tasks[start:stopp]
    
for player in list_players:
    print(player_tasks2latex_str(player))
    #print(f"{player.tasks}")

#with open("doc_template.tex", "r") as f:
    #full_string = f.read()
#print(full_string)
