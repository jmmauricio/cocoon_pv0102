from colinker.colinker import linker_run


if __name__ == "__main__":

    name = 'LINKER'
    mode = 'lmlm'
    cfg_dev = './emec_emu/pv_1_2_bess/config_devices_linker.json' 
    cfg_ctrl = './emec_emu/pv_1_2_bess/config_controller.json'

    linker_run(name, mode,cfg_dev, cfg_ctrl)
