
import subprocess
import json
import multiprocessing
from coppc.coppc import PPC
import coppc
        


import subprocess
import json
import multiprocessing

# sudo python3 run_devices_mininet_local.py
# sudo mnexec -a 1731 python3 run_device.py POI dmlm -cfg_dev ./config_devices_mininet_local.json -cfg_ctrl ./config_controller.json
# sudo mnexec -a 1733 python3 run_device.py LV0101 dmlm -cfg_dev ./config_devices_mininet_local.json -cfg_ctrl ./config_controller.json
# sudo mnexec -a 1735 python3 run_device.py LV0102 dmlm -cfg_dev ./config_devices_mininet_local.json -cfg_ctrl ./config_controller.json
# to free ports
# ps -fA | grep python

# sudo mnexec -a 41723 python3 ./mininet_local/run_ppc.py 


def run_in_host(json_file):
    # Read JSON data from file
    with open(json_file, "r") as fobj:
        hosts_dict = json.load(fobj)

    for item in hosts_dict:
        if item == 'PPC': 
            host_pid = hosts_dict[item]['pid']
            command = f"sudo mnexec -a {host_pid} python3 ./mininet_local/run_ppc.py"
            print(command)
            subprocess.run(command, shell=True)
            
if __name__ == "__main__":

    run_in_host('hosts.json')
