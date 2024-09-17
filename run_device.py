from colinker.colinker import linker_run
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="id name of the device")
    name = parser.id
    mode = 'dmlm'
    cfg_dev = './emec_emu/pv_1_2_bess/config_devices_linker.json' 
    cfg_ctrl = './emec_emu/pv_1_2_bess/config_controller.json'

    linker_run(name, mode,cfg_dev, cfg_ctrl)
