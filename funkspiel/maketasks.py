#!/bin/python

import json
import random
import string
import os
#global parameters for balancing etc.
#propabilities in percent if all are named here, else this is just a weighting factor
propability = {}
propability["Emergency"] = 1
propability["Get"] = 49
propability["Send"] = 50


def single_task(max_task_length, number_of_players, **task_values):
    """
    create a single task of any type
    """
    task = dict(**task_values)
    with open("Tasks/task_template.json") as f:
        task_template = json.load(f)

    #Randomly select a type from the template to be chosen as type of this new task
    if "task_type" not in task:
        task["task_type"] = random.choices(task_template["task_type"].split("/"))[0]
    #In case of emergency make the solution just a number based on 6 (highest number on standard dice) and the number of players
    if task["task_type"] == "Emergency":
        task["solution"] = random.randint(1, 6*number_of_players)
    else:
        task["solution"] = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=max_task_length))

    #print(task)
    return task


def make_tasks(number_of_players, number_of_tasks_per_player, max_task_length=10, save_folder="Tasks/Test/"):
    """
    Main Method to create tasks to later use in a game
    """
    number_of_tasks = number_of_players *  number_of_tasks_per_player
    with open("Tasks/task_template.json") as f:
        task_template = json.load(f)

    #print(task_template)
    #single_task(max_task_length, number_of_players, task_type="Emergency")
    #single_task(max_task_length, number_of_players)
    tasks_list =  []
    for i in range(0, number_of_tasks):
        tasks_list.append(single_task(max_task_length, number_of_players))
        tasks_list[i]["task_id"] = i
    if not os.path.isdir(save_folder):
       os.system(f"mv {save_folder}")
    for task in tasks_list:
        with open(save_folder + str(task["task_id"]) + ".json", "w") as f:
            json.dump(task, f)
    
    #print(tasks_list)
    return tasks_list


make_tasks(2, 20)