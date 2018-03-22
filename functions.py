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

    if t_list:
        tasks.append({name: t_list, parameters_name: lst})
        return tasks


def generate_probe_tasks(lst, task_list, clear_flag):
    if clear_flag:
        tasks.clear()

    for task in task_list:
        tasks.append({name: task, parameters_name: lst})
    return tasks


def generate_modules(lst, mname, clear_flag):
    if clear_flag:
        modules.clear()

    modules.append({name: mname, tasks_name: lst})
    return modules


def generate_agent(lst, branch):
    if agents:
        agents.clear()

    agents.append({key_name: agents_list[branch], modules_name: lst})
    return agents


def generate_level(lst, i, l_name, clear_flag):
    if clear_flag:
        levels.clear()

    levels.append({name: l_name, priority_name: i, agents_name: lst})
    return levels


def generate_file(lst, tsk):
    return {name: config_name, rules_name: rule, rcaSeverity_name: 5, originatorId_name: originatorId,
            taskKey_name: tsk, alertTypeName: alertType, levels_name: lst}
