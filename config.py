import paramiko
import xml.etree.ElementTree as ET

host = '192.168.12.214'
user = 'qladmin'
secret = 'DosduAffus6'
port = 10034

probe_config = {}
probe = 'probe1cbba8ffff18'


def get_config(t_probe):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command('cat /home/qladmin/scripts/RCA/' + t_probe + '/config.xml')
    data = stdout.read().decode('UTF-8')
    client.close()
    root = ET.fromstring(data)
    return root


def make_probe_config(root):
    for action in root.iter('Action'):
        pr_name = action.get('id')
        probe_config[pr_name] = []
        for task in action:
            task_name = task.get('id')
            probe_config[pr_name].append(task_name)
    return probe_config


# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname=host, username=user, password=secret, port=port)
# stdin, stdout, stderr = client.exec_command('cat /home/qladmin/scripts/RCA/' + probe + '/config.xml')
# data = stdout.read().decode('UTF-8')
# client.close()

# root_config = get_config(probe)
# print(make_probe_config(root_config))

# generate_level(copy.deepcopy(agents), 1, "level " + str("1"))
# data = generate_file(levels, 11)
#
# #print(data)
#
# with open(filename_work, "w", encoding="utf-8") as file:
#     json.dump(data, file)
