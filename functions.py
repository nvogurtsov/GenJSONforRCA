from init import *


def generate_params(md):
    i = 1
    if parameters:
        parameters.clear()

    for item in params_list[md]:
        parameters.append({name: item, priority_name: i})
        i = i + 1
    return parameters


def generate_tasks(lst, t_list, clear_flag):
    if clear_flag:
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
#     if len(t_list) >= 2:
#         tasks_lvl = t_list
#         for task in tasks_lvl:
#             tasks.append({name: task, parameters_name: lst})
#         return tasks
    if t_list:
        tasks.append({name: t_list, parameters_name: lst})
        return tasks


def generate_modules(lst, mname):
    if modules:
        modules.clear()

    modules.append({name: mname, tasks_name: lst})
    return modules


def generate_agent(lst, branch):
    if agents:
        agents.clear()

    agents.append({key_name: agents_list[branch], modules_name: lst})
    return agents


def generate_level(lst, i, l_name):
    levels.append({name: l_name, priority_name: i, agents_name: lst})
    return levels


def generate_file(lst, tsk):
    return {name: config_name, rules_name: rule, rcaSeverity_name: 5, originatorId_name: originatorId,
            taskKey_name: tsk, alertTypeName: alertType, levels_name: lst}
