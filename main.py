import json
import copy
from init import *


def generate_params(md):
    i = 1
    if parameters:
        parameters.clear()

    for item in params_list[md]:
        parameters.append({name: item, priority_name: i})
        i = i + 1
    return parameters


def generate_tasks(lst, t_list):
    if tasks:
        tasks.clear()

#    if i == 1:
#        tasks_lvl = tasks_list[0]
#        tasks.append({name: tasks_lvl, parameters_name: lst})
#        return tasks
#    elif i == 'full':
#        tasks_lvl = tasks_list[:]
#        for task in tasks_lvl:
#            tasks.append({name: task, parameters_name: lst})
#        return tasks
#    elif i == 2:
#        tasks_lvl = tasks_list[1:len(tasks_list)]
#        for task in tasks_lvl:
#            tasks.append({name: task, parameters_name: lst})
#        return tasks
    if len(t_list) >= 2:
        tasks_lvl = t_list
        for task in tasks_lvl:
            tasks.append({name: task, parameters_name: lst})
        return tasks
    elif len(t_list) == 1:
        tasks_lvl = t_list
        tasks.append({name: tasks_lvl, parameters_name: lst})
        return tasks


def generate_modules(lst):
    if modules:
        modules.clear()

    for module in modules_list:
        modules.append({name: module, tasks_name: lst})
    return modules


def generate_agent(lst):
    if agents:
        agents.clear()

    for agent in agents_list:
        agents.append({key_name: agent, modules_name: lst})
    return agents


def generate_level(lst, i, l_name):
    levels.append({name: l_name, priority_name: i, agents_name: lst})
    return levels


def generate_file(lst):
    return {name: "test", rules_name: ["L2"], rcaSeverity_name: 5, originatorId_name: originatorId,
            taskKey_name: taskKey, alertTypeName_name: alertTypeName, levels_name: lst}


#data1 = generate_agent(generate_modules(generate_tasks(generate_params("SNMPMonitor"), 1)))
#generate_level(copy.deepcopy(data1), 1, "main")

#data2 = generate_agent(generate_modules(generate_tasks(generate_params("SNMPMonitor"), 2)))
#generate_level(copy.deepcopy(data2), 2, "sub")

for it in range(0, len(tasks_list)):
    tmp_data = generate_agent(generate_modules(generate_tasks(generate_params("SNMPMonitor"), tasks_list[it:it+1])))
    generate_level(copy.deepcopy(tmp_data), it+1, "level " + str(it+1))

data = generate_file(levels)
#data = tasks

print(data)

with open("C:\Tecom\Qligent\RCA\gen\RCA.config", "w", encoding="utf-8") as file:
    json.dump(data, file)
