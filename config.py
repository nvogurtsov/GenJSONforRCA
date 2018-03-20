import paramiko
import xml.etree.ElementTree as ET
import copy
import json
from functions import *


host = '192.168.12.214'
user = 'qladmin'
secret = 'DosduAffus6'
port = 10034

probe = 'probe1cbba8ffff18'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('cat /home/qladmin/scripts/RCA/' + probe + '/config.xml')
data = stdout.read().decode('UTF-8')
client.close()

root = ET.fromstring(data)


def make_probe(t_branch):
    for action in root.iter('Action'):
        pr_name = action.get('id')
        for task in action:
            task_name = task.get('id')
            pr_priority = 1
            params_t = generate_params(pr_name)
            tasks_t = generate_tasks(copy.deepcopy(params_t), task_name, False)
            modules_t = generate_modules(tasks_t, pr_name)
            agents_t = generate_agent(modules_t, t_branch)
            #generate_level(copy.deepcopy(agents_t), pr_priority, "level " + str(pr_priority))
            #print(modules_t)
            print(tasks_t)


make_probe('Probe')
generate_level(copy.deepcopy(agents), 1, "level " + str("1"))
data = generate_file(levels, 11)

#print(data)

with open(filename_work, "w", encoding="utf-8") as file:
    json.dump(data, file)
