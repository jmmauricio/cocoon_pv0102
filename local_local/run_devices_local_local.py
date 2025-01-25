
import subprocess
import json
import multiprocessing

def run_command(device_id):

    command = f"python run_device.py {device_id} dmlm -cfg_dev ./local_local/config_devices_local_local.json -cfg_ctrl ./config_controller.json"
    print(command)
    subprocess.run(command, shell=True)
        
def run_devices(json_file):
    # Read JSON data from file
    with open(json_file, "r") as fobj:
        config = json.load(fobj)

    devices_list = config['devices']
    
    for item in devices_list:
        device_id = item['emec_id']
        process = multiprocessing.Process(target=run_command, args=(device_id,))
        process.start()
        
if __name__ == "__main__":
    json_file = './local_local/config_devices_local_local.json'
    run_devices(json_file)