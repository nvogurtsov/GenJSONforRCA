import json
import copy
from functions import *


def make_channel_config(t_module, t_branch):
    priority = len(tasks_list)
    for task in tasks_list:
        params_t = generate_params(t_module)
        tasks_t = generate_tasks(params_t, task)
        modules_t = generate_modules(tasks_t, t_module)
        agents_t = generate_agent(modules_t, t_branch)
        #tmp_data = generate_agent(generate_modules(generate_tasks(generate_params(module), task), module), branch)
        generate_level(copy.deepcopy(agents_t), priority, "level " + str(priority))
        priority -= 1


def make_probe_config(t_module, t_branch):
    pass


branch = "NN"
module = "SNMPMonitor"
taskKey = agents_list[branch] + "." + module + "." + tasks_list[0]

make_channel_config(module, branch)

data = generate_file(levels, taskKey)

print(data)

with open(filename_work, "w", encoding="utf-8") as file:
    json.dump(data, file)
