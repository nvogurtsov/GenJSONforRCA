import json
import copy
from config import *
from functions import *


def make_channel_config(t_module, t_branch):
    priority = len(tasks_list)
    for task in tasks_list:
        params_t = generate_params(t_module)
        tasks_t = generate_tasks(params_t, task, True)
        modules_t = generate_modules(tasks_t, t_module, True)
        agents_t = generate_agent(modules_t, t_branch)
        generate_level(copy.deepcopy(agents_t), priority, "level " + str(priority), False)
        priority -= 1


def make_probe_config(t_branch):
    for probe_module in parsed_config:
        params_t = generate_params(probe_module)
        tasks_t = generate_probe_tasks(copy.deepcopy(params_t), parsed_config[probe_module], True)
        modules_t = generate_modules(copy.deepcopy(tasks_t), probe_module, False)
        agents_t = generate_agent(modules_t, t_branch)
        generate_level(copy.deepcopy(agents_t), '1', "level " + str('1'), True)


branch = "NN"
module = "SNMPMonitor"
taskKey = agents_list[branch] + "." + module + "." + tasks_list[0]

make_channel_config(module, branch)
data = generate_file(levels, taskKey)

print(data)

with open(filename_work, "w", encoding="utf-8") as file:
    json.dump(data, file)
