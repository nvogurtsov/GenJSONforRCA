import paramiko
import elementtree.ElementTree as ET


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

#print(data)

tree = ET.ElementTree(data)
