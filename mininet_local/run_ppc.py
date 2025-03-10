
import subprocess
import json
import multiprocessing
from coppc.coppc import PPC
import coppc
        
if __name__ == "__main__":
    cfg_dev_path = './mininet_local/config_devices_mininet_local.json'
    cfg_ctrl_path=r'config_controller.json'
    print(coppc.__version__)
    ppc = PPC(cfg_dev_path,cfg_ctrl=cfg_ctrl_path) 
    ppc.Dt_mid = 0.2
    ppc.Dt_meas = 0.1
    ppc.K_qi = 0.8
    ppc.debug = True

    ppc.start_ctrl()
    ppc.start_api()