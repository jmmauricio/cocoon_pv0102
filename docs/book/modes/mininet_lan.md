# MININET-LAN mode

## Build emulator
    cd cocoon_pv0102
    cd ./emec_emu/pv_1_2_bess/
    python pv_mn_bess_builder.py 

## Run emulator 
    cd 
    python ./emec_emu/pv_1_2_bess/emulator.py -cfg_dev config_devices_mininet_lan.json -cfg_ctrl config_controller.json

## Run router
    python run_linker12.py -cfg_dev config_devices_mininet_lan_msi.json -cfg_ctrl config_controller.json

## Build mininet network in the Virtual Machine
    cd cocoon_pv0102
    sudo python3 ./com_emu/pv_1_2_mn.py

## Run device linkers 

Each linker is attached to the respective host:

    sudo python3 run_devices.py -cfg_dev config_devices_mininet_lan_msi.json -cfg_ctrl config_controller.json

## Test with PPC
    PPC python3 test_mininet_local.py
