
import subprocess
import json
import multiprocessing
from coppc.coppc import PPC
import coppc
        
if __name__ == "__main__":
    cfg_dev_path = './local_local/config_devices_local_local.json'
    cfg_ctrl_path=r'config_controller.json'
    print(coppc.__version__)
    ppc = PPC(cfg_dev_path,cfg_ctrl=cfg_ctrl_path) 
    ppc.start_ctrl()
    ppc.start_api()