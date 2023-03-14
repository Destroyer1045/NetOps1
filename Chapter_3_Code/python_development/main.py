from flask import Flask
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import yaml

app = Flask(__name__)

devices = {
    'lax-cor-r1': {'ip': '192.168.2.50', 'os': 'cisco_nxos' },
    'lax-edg-r1': {'ip': '192.168.2.51', 'os': 'cisco_ios'},
    'lax-edg-r2': {'ip': '192.168.2.52', 'os': 'cisco_ios'},
    'nyc-cor-r1': {'ip': '192.168.2.60', 'os': 'cisco_nxos'},
    'nyc-edg-r1': {'ip': '192.168.2.61', 'os': 'cisco_ios'},
    'nyc-edg-r2': {'ip': '192.168.2.62', 'os': 'cisco_ios'},
}

@app.route('/')
def index():
    return 'You are at root'


@app.route('/device/<hostname>/version')
def show_version(hostname):

    # retreive correct value
    values = {
        hostname: {
            'hostname': devices[hostname]['ip'],
            'port': 22,
            'username': 'cisco',
            'password': 'cisco',
            'platform': devices[hostname]['os']
        }
    }

    # write to hosts.yaml file 
    with open('hosts.yaml', 'w') as f: 
        yaml.dump(values, f)

    # initialize Nornir
    nr = InitNornir(
        inventory={
            "options": {
                "host_file": "hosts.yaml"
            }
        }
    )

    # return show version result 
    result = nr.run(
        task=netmiko_send_command,
        command_string="show version"
    )

    return str(result[hostname][0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

