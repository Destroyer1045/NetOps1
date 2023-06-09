#!/usr/bin/env python
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

# Initialize Nornir, by default it will look for the 
# hosts.yaml file in the same directory. 
nr = InitNornir()

# Run the show version command for each of the devices. 
# store the value in the results variable. 
result = nr.run(
    task=netmiko_send_command,
    command_string="show version"
)

# print the results in 
#print_result(result)

# Nornir documentation on multi-result objects
# https://nornir.readthedocs.io/en/latest/tutorial/task_results.html
for i in result.keys(): 
    with open(str(i), 'w') as f:
        f.write(str(result[i][0]))

