import json
import copy
from functions import *


module = "SNMPMonitor"
branch = "NN"
priority = len(tasks_list)

for channel in tasks_list:
    tmp_data = generate_agent(generate_modules(generate_tasks(generate_params(module), channel), module), branch)
    generate_level(copy.deepcopy(tmp_data), priority, "level " + str(priority))
    priority -= 1

data = generate_file(levels)

print(data)

with open(filename_work, "w", encoding="utf-8") as file:
    json.dump(data, file)
