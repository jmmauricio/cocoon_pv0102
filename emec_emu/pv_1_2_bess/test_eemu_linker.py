from colinker.colinker import Linker,modbus_server
from multiprocessing import Process

name = 'LINKER'
mode = 'lmev'

cfg_dev = "../../local_local/config_devices_local_local.json"
cfg_ctrl = "../../config_controller.json"

link = Linker(name, cfg_dev, cfg_ctrl)
link.setup_multiple_device()

print(link.measurements_dict)
