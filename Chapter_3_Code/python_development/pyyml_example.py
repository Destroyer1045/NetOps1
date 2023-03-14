#!/usr/bin/env python
import yaml

# Create dictionary for values
values = {
    'iosv-1': {
        'hostname': '192.168.2.71',
        'port': 22,
        'username': 'cisco',
        'password': 'cisco',
        'platform': 'cisco_ios'
    }
}

# Write to hosts.yaml file 
with open('hosts.yaml', 'w') as f: 
    yaml.dump(values, f)

