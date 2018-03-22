import paramiko
import xml.etree.ElementTree as ET

parsed_config = {}

host = '192.168.12.214'
user = ''
secret = ''
port = 10034
rca_dir = '/home/qladmin/scripts/RCA/'
probe = 'probe1cbba8ffff18'


def copy_probe_config(t_probe):
    f_client = paramiko.SSHClient()
    f_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    f_client.connect(hostname=host, username=user, password=secret, port=port)
    f_client.exec_command('mkdir -p ' + rca_dir + t_probe)
    f_client.exec_command('scp support@' + t_probe +
                          '.node.qos:/opt/qligent/vision/Conf/XMLCFG/config.xml ' + rca_dir)
    f_client.close()


def get_probe_config(t_probe):
    f_client = paramiko.SSHClient()
    f_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    f_client.connect(hostname=host, username=user, password=secret, port=port)
    f_stdin, f_stdout, f_stderr = f_client.exec_command('cat ' + rca_dir + t_probe + '/config.xml')
    data = f_stdout.read().decode('UTF-8')
    f_client.close()
    return data


def make_probe_config(data):
    root = ET.fromstring(data)
    for action in root.iter('Action'):
        pr_name = action.get('id')
        parsed_config[pr_name] = []
        for p_task in action:
            task_name = p_task.get('id')
            parsed_config[pr_name].append(task_name)
    return parsed_config


copy_probe_config(probe)
text_config = get_probe_config(probe)
make_probe_config(text_config)

# for module in parsed_config:
#     params_t = generate_params(module)
#     tasks_t = generate_probe_tasks(copy.deepcopy(params_t), parsed_config[module], True)
#     modules_t = generate_modules(copy.deepcopy(tasks_t), module, False)
#     agents_t = generate_agent(modules_t, 'Probe')
#     generate_level(copy.deepcopy(agents_t), '1', "level " + str('1'), True)
#     rca_config = generate_file(levels, "Test Task Key")
