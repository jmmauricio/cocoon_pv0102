# cocoon_pv0102
PV plant PV 1x2


## Local-Local mode

    cd cocoon_pv0102
    python ./emec_emu/pv_1_2_bess/emulator.py -cfg_dev config_devices_local_local.json -cfg_ctrl config_controller.json
    python run_device.py POI dmlm -cfg_dev config_devices_local_local.json -cfg_ctrl config_controller.json
    python run_device.py LV0101 dmlm -cfg_dev config_devices_local_local.json -cfg_ctrl config_controller.json
    python run_device.py LV0102 dmlm -cfg_dev config_devices_local_local.json -cfg_ctrl config_controller.json

Some tests can be done using `test_local_local.py` module. 


## MININET-Local mode

    python ./emec_emu/pv_1_2_bess/emulator.py -cfg_dev config_devices_mininet_local.json -cfg_ctrl config_controller.json

    git clone https://github.com/jmmauricio/colinker.git
    cd colinker
    sudo pip3 install -e  . --break-system-packages

    git clone https://github.com/jmmauricio/cocoon_pv0102.git

    cd cocoon_pv0102
    sudo python3 ./com_emu/pv_1_2_mn.py
    POI python3 run_device.py 'POI' dmlm -cfg_dev config_devices_mininet_local.json -cfg_ctrl config_controller.json
    python run_device.py 'LV0101' dmlm -cfg_dev config_devices_mininet_local.json -cfg_ctrl config_controller.json
    python run_device.py 'LV0102' dmlm -cfg_dev config_devices_mininet_local.json -cfg_ctrl config_controller.json

Some tests can be done using `test_mininet_local.py` module.  (to_do)


## MININET-LAN mode

    python ./emec_emu/pv_1_2_bess/emulator.py -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json
    python run_linker12.py -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json


    python run_device.py 'POI' dmlm -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json
    python ./emec_emu/pv_1_2_bess/emulator.py -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json

    git clone https://github.com/jmmauricio/colinker.git
    cd colinker
    sudo pip3 install -e  . --break-system-packages

    git clone https://github.com/jmmauricio/cocoon_pv0102.git

    cd cocoon_pv0102
    sudo python3 ./com_emu/pv_1_2_mn.py
    POI python3 run_device.py 'POI' dmlm -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json
    python run_device.py 'LV0101' dmlm -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json
    python run_device.py 'LV0102' dmlm -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json

Some tests can be done using `test_mininet_local.py` module.  (to_do)