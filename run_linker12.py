from colinker.colinker import linker_run
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-cfg_dev", help="id name of the device")
    parser.add_argument("-cfg_ctrl", help="id name of the device")
    args = parser.parse_args()

    linker_run('LINKER12', 'lmlm', args.cfg_dev, args.cfg_ctrl)


