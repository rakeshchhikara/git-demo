import time  # Importing time module to check total runtime.
import pandas  # Importing pandas module to convert csv rows to individual lists based on first row headers.
from netmiko import ConnectHandler  # for connecting and configuring device
import getpass


def initial_func(user_prompt):
    lines = []
    while True:
        line = input(user_prompt)

        if line:
            lines.append(line)
        else:
            break
    return lines


# Capturing start time
start = time.time()

# Converting csv rows to individual lists based on first row headers.
devices_list = pandas.read_csv("device_details.csv", header=0)
ip_s = list(devices_list.Ip_Address)

print(ip_s)

failed_list = []

username = input("Enter Username for device Login: ")
password = getpass.getpass(prompt="Enter device password: ")
# password = input("Enter device password: ")
user_prompt = "Enter show command: "

lines = initial_func(user_prompt)

print(lines)

for ip in ip_s:
    device = {
        'device_type': 'cisco_xr',
        'host': ip,
        'username': username,
        'password': password,
        'port': 22,  # optional, default 22
        'verbose': True  # optional, default False
    }

    connection = ConnectHandler(**device)
    prompt = connection.find_prompt()
    prompt_strip = prompt.find(':') + 1
    hostname = prompt[prompt_strip:-1]

    filename = hostname+".txt"

    with open(filename, 'w') as logs:
        for each_command in lines:
            output = connection.send_command(each_command, max_loops=50000, delay_factor=5, strip_command=False,
                                             strip_prompt=False)
            print(output)
            if '         ^' in output:
                failed_list.append(each_command)
            logs.write(f'{prompt}{output}\n{100 * "#"}\n')

        print(f'List of Failed show commands {failed_list}')
        print(120 * "#")


