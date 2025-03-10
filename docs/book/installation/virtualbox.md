# VirtualBox VM

At least 3 network adapters:

- NAT for internet conection (not used in the emulation)
- Host Only to connect the mininet network to the e-emulator running at the host
- Bridge to connect to a physical adapter and access to the mininet network (virtual actual side), that can be used to a man in the middle atack or by the CPN.

![alt text](./figs/vm_adapters.png)

![alt text](./figs/vm_hostonly.png)

## COLinker installation

    git clone https://github.com/jmmauricio/colinker.git
    cd colinker
    sudo pip3 install -e  . --break-system-packages

## COPPC installation

    git clone https://github.com/jmmauricio/coppc.git
    cd coppc
    sudo pip3 install -e  . --break-system-packages

## Clone example PV 1x2 repo

    git clone https://github.com/jmmauricio/cocoon_pv0102.git

