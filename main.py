import json
import copy
from functions import *


def gen_channels(module, branch):
    priority = len(tasks_list)
    for task in tasks_list:
        tmp_data = generate_agent(generate_modules(generate_tasks(generate_params(module), task), module), branch)
        generate_level(copy.deepcopy(tmp_data), priority, "level " + str(priority))
        priority -= 1


gen_channels("SNMPMonitor", "NN")

data = generate_file(levels)

print(data)

with open(filename_work, "w", encoding="utf-8") as file:
    json.dump(data, file)
